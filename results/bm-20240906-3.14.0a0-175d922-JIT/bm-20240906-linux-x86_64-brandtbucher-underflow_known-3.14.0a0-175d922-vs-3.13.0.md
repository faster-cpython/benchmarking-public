# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_known
- machine: linux-x86_64
- commit hash: 175d922
- commit date: 2024-09-06
- overall geometric mean: 1.029x faster
- HPT reliability: 70.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 276 ms: 1.04x slower                                                   |
| docutils       | 2.59 sec                                               | 3.01 sec: 1.16x slower                                                 |
| html5lib       | 64.2 ms                                                | 64.8 ms: 1.01x slower                                                  |
| tornado_http   | 92.4 ms                                                | 97.0 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 405 ms: 1.14x faster                                                   |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                                   |
| async_tree_none           | 351 ms                                                 | 326 ms: 1.07x faster                                                   |
| async_tree_none_tg        | 321 ms                                                 | 309 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 567 ms: 1.02x faster                                                   |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                                   |
| coroutines                | 22.7 ms                                                | 23.0 ms: 1.01x slower                                                  |
| async_tree_io_tg          | 857 ms                                                 | 898 ms: 1.05x slower                                                   |
| async_generators          | 436 ms                                                 | 460 ms: 1.06x slower                                                   |
| async_tree_io             | 842 ms                                                 | 938 ms: 1.11x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.3 ms: 1.13x faster                                                  |
| nbody          | 87.0 ms                                                | 79.5 ms: 1.09x faster                                                  |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                  |
| regex_effbot   | 3.73 ms                                                | 3.71 ms: 1.01x faster                                                  |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                                   |
| regex_compile  | 132 ms                                                 | 142 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.8 ms: 1.12x faster                                                  |
| tomli_loads          | 2.14 sec                                               | 1.92 sec: 1.11x faster                                                 |
| xml_etree_process    | 60.6 ms                                                | 55.3 ms: 1.10x faster                                                  |
| unpickle_pure_python | 216 us                                                 | 199 us: 1.08x faster                                                   |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                   |
| pickle_pure_python   | 310 us                                                 | 300 us: 1.03x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 98.6 ms: 1.03x faster                                                  |
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                  |
| json_loads           | 27.2 us                                                | 28.2 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                  |
| python_startup_no_site | 6.96 ms                                                | 7.16 ms: 1.03x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.81 ms: 1.13x faster                                                  |
| django_template | 35.2 ms                                                | 36.2 ms: 1.03x slower                                                  |
| genshi_text     | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                  |
| genshi_xml      | 50.9 ms                                                | 57.3 ms: 1.13x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 26.0 us: 1.50x faster                                                  |
| create_gc_cycles          | 2.41 ms                                                | 1.77 ms: 1.36x faster                                                  |
| deepcopy                  | 358 us                                                 | 264 us: 1.36x faster                                                   |
| richards_super            | 54.9 ms                                                | 42.6 ms: 1.29x faster                                                  |
| richards                  | 48.7 ms                                                | 40.0 ms: 1.22x faster                                                  |
| deepcopy_reduce           | 3.20 us                                                | 2.64 us: 1.21x faster                                                  |
| gc_traversal              | 4.37 ms                                                | 3.66 ms: 1.19x faster                                                  |
| scimark_fft               | 364 ms                                                 | 305 ms: 1.19x faster                                                   |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.23 ms: 1.19x faster                                                  |
| python_startup            | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                  |
| spectral_norm             | 115 ms                                                 | 99.7 ms: 1.16x faster                                                  |
| async_tree_memoization_tg | 464 ms                                                 | 405 ms: 1.14x faster                                                   |
| mako                      | 11.1 ms                                                | 9.81 ms: 1.13x faster                                                  |
| float                     | 79.2 ms                                                | 70.3 ms: 1.13x faster                                                  |
| crypto_pyaes              | 75.3 ms                                                | 66.9 ms: 1.13x faster                                                  |
| xml_etree_generate        | 86.7 ms                                                | 77.8 ms: 1.12x faster                                                  |
| tomli_loads               | 2.14 sec                                               | 1.92 sec: 1.11x faster                                                 |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                                   |
| pathlib                   | 17.5 ms                                                | 16.0 ms: 1.10x faster                                                  |
| xml_etree_process         | 60.6 ms                                                | 55.3 ms: 1.10x faster                                                  |
| nbody                     | 87.0 ms                                                | 79.5 ms: 1.09x faster                                                  |
| go                        | 144 ms                                                 | 132 ms: 1.09x faster                                                   |
| unpickle_pure_python      | 216 us                                                 | 199 us: 1.08x faster                                                   |
| logging_silent            | 102 ns                                                 | 94.5 ns: 1.08x faster                                                  |
| fannkuch                  | 404 ms                                                 | 376 ms: 1.08x faster                                                   |
| async_tree_none           | 351 ms                                                 | 326 ms: 1.07x faster                                                   |
| scimark_sor               | 124 ms                                                 | 115 ms: 1.07x faster                                                   |
| bpe_tokeniser             | 4.75 sec                                               | 4.42 sec: 1.07x faster                                                 |
| telco                     | 8.54 ms                                                | 7.97 ms: 1.07x faster                                                  |
| mdp                       | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                 |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                   |
| regex_v8                  | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                  |
| pyflate                   | 471 ms                                                 | 450 ms: 1.05x faster                                                   |
| thrift                    | 809 us                                                 | 778 us: 1.04x faster                                                   |
| async_tree_none_tg        | 321 ms                                                 | 309 ms: 1.04x faster                                                   |
| scimark_lu                | 113 ms                                                 | 109 ms: 1.03x faster                                                   |
| pickle_pure_python        | 310 us                                                 | 300 us: 1.03x faster                                                   |
| logging_format            | 6.40 us                                                | 6.19 us: 1.03x faster                                                  |
| xml_etree_iterparse       | 101 ms                                                 | 98.6 ms: 1.03x faster                                                  |
| json_dumps                | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                  |
| meteor_contest            | 109 ms                                                 | 107 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 567 ms: 1.02x faster                                                   |
| logging_simple            | 5.72 us                                                | 5.64 us: 1.01x faster                                                  |
| json                      | 5.36 ms                                                | 5.30 ms: 1.01x faster                                                  |
| regex_effbot              | 3.73 ms                                                | 3.71 ms: 1.01x faster                                                  |
| pidigits                  | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                                   |
| pycparser                 | 1.20 sec                                               | 1.21 sec: 1.01x slower                                                 |
| html5lib                  | 64.2 ms                                                | 64.8 ms: 1.01x slower                                                  |
| regex_dna                 | 218 ms                                                 | 221 ms: 1.01x slower                                                   |
| coroutines                | 22.7 ms                                                | 23.0 ms: 1.01x slower                                                  |
| raytrace                  | 267 ms                                                 | 272 ms: 1.02x slower                                                   |
| coverage                  | 84.0 ms                                                | 86.0 ms: 1.02x slower                                                  |
| bench_thread_pool         | 822 us                                                 | 842 us: 1.02x slower                                                   |
| chaos                     | 58.1 ms                                                | 59.7 ms: 1.03x slower                                                  |
| python_startup_no_site    | 6.96 ms                                                | 7.16 ms: 1.03x slower                                                  |
| django_template           | 35.2 ms                                                | 36.2 ms: 1.03x slower                                                  |
| genshi_text               | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                  |
| 2to3                      | 267 ms                                                 | 276 ms: 1.04x slower                                                   |
| json_loads                | 27.2 us                                                | 28.2 us: 1.04x slower                                                  |
| sqlglot_normalize         | 108 ms                                                 | 112 ms: 1.04x slower                                                   |
| async_tree_io_tg          | 857 ms                                                 | 898 ms: 1.05x slower                                                   |
| tornado_http              | 92.4 ms                                                | 97.0 ms: 1.05x slower                                                  |
| async_generators          | 436 ms                                                 | 460 ms: 1.06x slower                                                   |
| dulwich_log               | 64.3 ms                                                | 68.5 ms: 1.07x slower                                                  |
| regex_compile             | 132 ms                                                 | 142 ms: 1.08x slower                                                   |
| sqlglot_parse             | 1.27 ms                                                | 1.37 ms: 1.08x slower                                                  |
| sqlglot_transpile         | 1.58 ms                                                | 1.71 ms: 1.08x slower                                                  |
| sqlglot_optimize          | 53.7 ms                                                | 58.3 ms: 1.08x slower                                                  |
| nqueens                   | 78.4 ms                                                | 85.2 ms: 1.09x slower                                                  |
| sympy_str                 | 275 ms                                                 | 299 ms: 1.09x slower                                                   |
| sympy_expand              | 463 ms                                                 | 507 ms: 1.09x slower                                                   |
| async_tree_io             | 842 ms                                                 | 938 ms: 1.11x slower                                                   |
| hexiom                    | 6.16 ms                                                | 6.88 ms: 1.12x slower                                                  |
| genshi_xml                | 50.9 ms                                                | 57.3 ms: 1.13x slower                                                  |
| sympy_sum                 | 150 ms                                                 | 172 ms: 1.14x slower                                                   |
| sympy_integrate           | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                  |
| generators                | 29.0 ms                                                | 33.3 ms: 1.15x slower                                                  |
| docutils                  | 2.59 sec                                               | 3.01 sec: 1.16x slower                                                 |
| pylint                    | 313 ms                                                 | 372 ms: 1.19x slower                                                   |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (8): pprint_safe_repr, deltablue, typing_runtime_protocols, bench_mp_pool, comprehensions, async_tree_cpu_io_mixed_tg, scimark_monte_carlo, pprint_pformat
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240906-3.14.0a0-175d922-JIT/bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.029x faster
# HPT report

- Reliability score: 70.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x