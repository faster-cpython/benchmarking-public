# Results vs. 3.13.0

- fork: brandtbucher
- ref: trace_through
- machine: linux-x86_64
- commit hash: b1a2c42
- commit date: 2024-09-06
- overall geometric mean: 1.027x faster
- HPT reliability: 91.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 278 ms: 1.04x slower                                                 |
| docutils       | 2.59 sec                                               | 3.00 sec: 1.16x slower                                               |
| html5lib       | 64.2 ms                                                | 62.4 ms: 1.03x faster                                                |
| tornado_http   | 92.4 ms                                                | 95.7 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 401 ms: 1.16x faster                                                 |
| async_tree_memoization    | 442 ms                                                 | 402 ms: 1.10x faster                                                 |
| async_tree_none           | 351 ms                                                 | 325 ms: 1.08x faster                                                 |
| async_tree_none_tg        | 321 ms                                                 | 307 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 562 ms: 1.03x faster                                                 |
| asyncio_websockets        | 552 ms                                                 | 554 ms: 1.00x slower                                                 |
| coroutines                | 22.7 ms                                                | 23.0 ms: 1.02x slower                                                |
| async_tree_io_tg          | 857 ms                                                 | 889 ms: 1.04x slower                                                 |
| async_generators          | 436 ms                                                 | 460 ms: 1.06x slower                                                 |
| async_tree_io             | 842 ms                                                 | 926 ms: 1.10x slower                                                 |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.3 ms: 1.13x faster                                                |
| nbody          | 87.0 ms                                                | 81.0 ms: 1.07x faster                                                |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.47 ms: 1.07x faster                                                |
| regex_v8       | 26.2 ms                                                | 24.4 ms: 1.07x faster                                                |
| regex_dna      | 218 ms                                                 | 212 ms: 1.03x faster                                                 |
| regex_compile  | 132 ms                                                 | 145 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 76.5 ms: 1.13x faster                                                |
| xml_etree_process    | 60.6 ms                                                | 54.0 ms: 1.12x faster                                                |
| tomli_loads          | 2.14 sec                                               | 1.95 sec: 1.10x faster                                               |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 98.5 ms: 1.03x faster                                                |
| pickle_pure_python   | 310 us                                                 | 302 us: 1.03x faster                                                 |
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                |
| unpickle_pure_python | 216 us                                                 | 213 us: 1.01x faster                                                 |
| json_loads           | 27.2 us                                                | 28.7 us: 1.05x slower                                                |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                |
| python_startup_no_site | 6.96 ms                                                | 7.17 ms: 1.03x slower                                                |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.85 ms: 1.13x faster                                                |
| django_template | 35.2 ms                                                | 36.6 ms: 1.04x slower                                                |
| genshi_text     | 23.5 ms                                                | 24.5 ms: 1.04x slower                                                |
| genshi_xml      | 50.9 ms                                                | 55.9 ms: 1.10x slower                                                |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 26.4 us: 1.48x faster                                                |
| create_gc_cycles          | 2.41 ms                                                | 1.76 ms: 1.37x faster                                                |
| deepcopy                  | 358 us                                                 | 264 us: 1.35x faster                                                 |
| richards_super            | 54.9 ms                                                | 44.0 ms: 1.25x faster                                                |
| richards                  | 48.7 ms                                                | 39.8 ms: 1.22x faster                                                |
| deepcopy_reduce           | 3.20 us                                                | 2.62 us: 1.22x faster                                                |
| gc_traversal              | 4.37 ms                                                | 3.59 ms: 1.22x faster                                                |
| python_startup            | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                |
| async_tree_memoization_tg | 464 ms                                                 | 401 ms: 1.16x faster                                                 |
| scimark_fft               | 364 ms                                                 | 316 ms: 1.15x faster                                                 |
| spectral_norm             | 115 ms                                                 | 100 ms: 1.15x faster                                                 |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.43 ms: 1.14x faster                                                |
| xml_etree_generate        | 86.7 ms                                                | 76.5 ms: 1.13x faster                                                |
| crypto_pyaes              | 75.3 ms                                                | 66.7 ms: 1.13x faster                                                |
| float                     | 79.2 ms                                                | 70.3 ms: 1.13x faster                                                |
| mako                      | 11.1 ms                                                | 9.85 ms: 1.13x faster                                                |
| xml_etree_process         | 60.6 ms                                                | 54.0 ms: 1.12x faster                                                |
| pathlib                   | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                |
| async_tree_memoization    | 442 ms                                                 | 402 ms: 1.10x faster                                                 |
| tomli_loads               | 2.14 sec                                               | 1.95 sec: 1.10x faster                                               |
| fannkuch                  | 404 ms                                                 | 374 ms: 1.08x faster                                                 |
| async_tree_none           | 351 ms                                                 | 325 ms: 1.08x faster                                                 |
| scimark_monte_carlo       | 67.4 ms                                                | 62.7 ms: 1.08x faster                                                |
| regex_effbot              | 3.73 ms                                                | 3.47 ms: 1.07x faster                                                |
| nbody                     | 87.0 ms                                                | 81.0 ms: 1.07x faster                                                |
| regex_v8                  | 26.2 ms                                                | 24.4 ms: 1.07x faster                                                |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.07x faster                                                 |
| go                        | 144 ms                                                 | 134 ms: 1.07x faster                                                 |
| telco                     | 8.54 ms                                                | 7.99 ms: 1.07x faster                                                |
| scimark_sor               | 124 ms                                                 | 116 ms: 1.06x faster                                                 |
| bpe_tokeniser             | 4.75 sec                                               | 4.50 sec: 1.05x faster                                               |
| pyflate                   | 471 ms                                                 | 449 ms: 1.05x faster                                                 |
| async_tree_none_tg        | 321 ms                                                 | 307 ms: 1.04x faster                                                 |
| deltablue                 | 3.23 ms                                                | 3.11 ms: 1.04x faster                                                |
| thrift                    | 809 us                                                 | 780 us: 1.04x faster                                                 |
| regex_dna                 | 218 ms                                                 | 212 ms: 1.03x faster                                                 |
| logging_format            | 6.40 us                                                | 6.22 us: 1.03x faster                                                |
| html5lib                  | 64.2 ms                                                | 62.4 ms: 1.03x faster                                                |
| xml_etree_iterparse       | 101 ms                                                 | 98.5 ms: 1.03x faster                                                |
| pickle_pure_python        | 310 us                                                 | 302 us: 1.03x faster                                                 |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 562 ms: 1.03x faster                                                 |
| json_dumps                | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                |
| logging_silent            | 102 ns                                                 | 100.0 ns: 1.02x faster                                               |
| pprint_safe_repr          | 728 ms                                                 | 716 ms: 1.02x faster                                                 |
| unpickle_pure_python      | 216 us                                                 | 213 us: 1.01x faster                                                 |
| pycparser                 | 1.20 sec                                               | 1.19 sec: 1.01x faster                                               |
| json                      | 5.36 ms                                                | 5.30 ms: 1.01x faster                                                |
| logging_simple            | 5.72 us                                                | 5.67 us: 1.01x faster                                                |
| asyncio_websockets        | 552 ms                                                 | 554 ms: 1.00x slower                                                 |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                 |
| typing_runtime_protocols  | 165 us                                                 | 167 us: 1.01x slower                                                 |
| bench_thread_pool         | 822 us                                                 | 834 us: 1.02x slower                                                 |
| comprehensions            | 16.5 us                                                | 16.7 us: 1.02x slower                                                |
| coroutines                | 22.7 ms                                                | 23.0 ms: 1.02x slower                                                |
| coverage                  | 84.0 ms                                                | 85.8 ms: 1.02x slower                                                |
| raytrace                  | 267 ms                                                 | 274 ms: 1.03x slower                                                 |
| python_startup_no_site    | 6.96 ms                                                | 7.17 ms: 1.03x slower                                                |
| tornado_http              | 92.4 ms                                                | 95.7 ms: 1.04x slower                                                |
| async_tree_io_tg          | 857 ms                                                 | 889 ms: 1.04x slower                                                 |
| django_template           | 35.2 ms                                                | 36.6 ms: 1.04x slower                                                |
| genshi_text               | 23.5 ms                                                | 24.5 ms: 1.04x slower                                                |
| 2to3                      | 267 ms                                                 | 278 ms: 1.04x slower                                                 |
| sqlglot_parse             | 1.27 ms                                                | 1.33 ms: 1.04x slower                                                |
| sqlglot_normalize         | 108 ms                                                 | 113 ms: 1.05x slower                                                 |
| sqlglot_transpile         | 1.58 ms                                                | 1.67 ms: 1.05x slower                                                |
| json_loads                | 27.2 us                                                | 28.7 us: 1.05x slower                                                |
| async_generators          | 436 ms                                                 | 460 ms: 1.06x slower                                                 |
| sqlglot_optimize          | 53.7 ms                                                | 58.4 ms: 1.09x slower                                                |
| sympy_expand              | 463 ms                                                 | 507 ms: 1.09x slower                                                 |
| regex_compile             | 132 ms                                                 | 145 ms: 1.10x slower                                                 |
| genshi_xml                | 50.9 ms                                                | 55.9 ms: 1.10x slower                                                |
| nqueens                   | 78.4 ms                                                | 86.1 ms: 1.10x slower                                                |
| dulwich_log               | 64.3 ms                                                | 70.7 ms: 1.10x slower                                                |
| async_tree_io             | 842 ms                                                 | 926 ms: 1.10x slower                                                 |
| sympy_str                 | 275 ms                                                 | 304 ms: 1.11x slower                                                 |
| generators                | 29.0 ms                                                | 33.0 ms: 1.14x slower                                                |
| sympy_integrate           | 19.9 ms                                                | 23.0 ms: 1.16x slower                                                |
| docutils                  | 2.59 sec                                               | 3.00 sec: 1.16x slower                                               |
| sympy_sum                 | 150 ms                                                 | 175 ms: 1.17x slower                                                 |
| pylint                    | 313 ms                                                 | 374 ms: 1.20x slower                                                 |
| hexiom                    | 6.16 ms                                                | 7.73 ms: 1.25x slower                                                |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, pprint_pformat, mdp, bench_mp_pool, meteor_contest, scimark_lu, chaos
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240906-3.14.0a0-b1a2c42-JIT/bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 91.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x