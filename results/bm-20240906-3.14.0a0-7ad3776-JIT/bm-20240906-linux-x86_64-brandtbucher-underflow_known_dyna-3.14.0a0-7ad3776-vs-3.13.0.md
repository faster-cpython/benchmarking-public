# Results vs. 3.13.0

- fork: brandtbucher
- ref: underflow_known_dyna
- machine: linux-x86_64
- commit hash: 7ad3776
- commit date: 2024-09-06
- overall geometric mean: 1.010x faster
- HPT reliability: 56.90%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 285 ms: 1.07x slower                                                        |
| docutils       | 2.59 sec                                               | 3.25 sec: 1.25x slower                                                      |
| html5lib       | 64.2 ms                                                | 69.1 ms: 1.08x slower                                                       |
| tornado_http   | 92.4 ms                                                | 103 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                  | 1.13x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 406 ms: 1.14x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 406 ms: 1.09x faster                                                        |
| async_tree_none           | 351 ms                                                 | 326 ms: 1.08x faster                                                        |
| async_tree_none_tg        | 321 ms                                                 | 311 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 563 ms: 1.03x faster                                                        |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                        |
| coroutines                | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                       |
| async_tree_io_tg          | 857 ms                                                 | 900 ms: 1.05x slower                                                        |
| async_generators          | 436 ms                                                 | 460 ms: 1.06x slower                                                        |
| async_tree_io             | 842 ms                                                 | 933 ms: 1.11x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.9 ms: 1.12x faster                                                       |
| nbody          | 87.0 ms                                                | 79.6 ms: 1.09x faster                                                       |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.6 ms: 1.07x faster                                                       |
| regex_effbot   | 3.73 ms                                                | 3.62 ms: 1.03x faster                                                       |
| regex_dna      | 218 ms                                                 | 216 ms: 1.01x faster                                                        |
| regex_compile  | 132 ms                                                 | 151 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 54.3 ms: 1.12x faster                                                       |
| xml_etree_generate   | 86.7 ms                                                | 77.8 ms: 1.12x faster                                                       |
| unpickle_pure_python | 216 us                                                 | 201 us: 1.07x faster                                                        |
| tomli_loads          | 2.14 sec                                               | 2.00 sec: 1.07x faster                                                      |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                                       |
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                       |
| json_loads           | 27.2 us                                                | 28.5 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                       |
| python_startup_no_site | 6.96 ms                                                | 7.17 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.70 ms: 1.14x faster                                                       |
| genshi_text     | 23.5 ms                                                | 23.9 ms: 1.01x slower                                                       |
| django_template | 35.2 ms                                                | 37.9 ms: 1.08x slower                                                       |
| genshi_xml      | 50.9 ms                                                | 63.5 ms: 1.25x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776 |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 26.0 us: 1.51x faster                                                       |
| deepcopy                  | 358 us                                                 | 263 us: 1.36x faster                                                        |
| create_gc_cycles          | 2.41 ms                                                | 1.78 ms: 1.35x faster                                                       |
| richards_super            | 54.9 ms                                                | 42.8 ms: 1.28x faster                                                       |
| richards                  | 48.7 ms                                                | 38.4 ms: 1.27x faster                                                       |
| deepcopy_reduce           | 3.20 us                                                | 2.64 us: 1.21x faster                                                       |
| scimark_fft               | 364 ms                                                 | 309 ms: 1.18x faster                                                        |
| python_startup            | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                       |
| gc_traversal              | 4.37 ms                                                | 3.78 ms: 1.16x faster                                                       |
| spectral_norm             | 115 ms                                                 | 99.9 ms: 1.15x faster                                                       |
| crypto_pyaes              | 75.3 ms                                                | 65.4 ms: 1.15x faster                                                       |
| async_tree_memoization_tg | 464 ms                                                 | 406 ms: 1.14x faster                                                        |
| mako                      | 11.1 ms                                                | 9.70 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.44 ms: 1.13x faster                                                       |
| float                     | 79.2 ms                                                | 70.9 ms: 1.12x faster                                                       |
| xml_etree_process         | 60.6 ms                                                | 54.3 ms: 1.12x faster                                                       |
| xml_etree_generate        | 86.7 ms                                                | 77.8 ms: 1.12x faster                                                       |
| pathlib                   | 17.5 ms                                                | 15.9 ms: 1.11x faster                                                       |
| nbody                     | 87.0 ms                                                | 79.6 ms: 1.09x faster                                                       |
| telco                     | 8.54 ms                                                | 7.83 ms: 1.09x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 406 ms: 1.09x faster                                                        |
| async_tree_none           | 351 ms                                                 | 326 ms: 1.08x faster                                                        |
| mdp                       | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                      |
| unpickle_pure_python      | 216 us                                                 | 201 us: 1.07x faster                                                        |
| tomli_loads               | 2.14 sec                                               | 2.00 sec: 1.07x faster                                                      |
| bpe_tokeniser             | 4.75 sec                                               | 4.45 sec: 1.07x faster                                                      |
| regex_v8                  | 26.2 ms                                                | 24.6 ms: 1.07x faster                                                       |
| fannkuch                  | 404 ms                                                 | 382 ms: 1.06x faster                                                        |
| xml_etree_parse           | 156 ms                                                 | 148 ms: 1.05x faster                                                        |
| go                        | 144 ms                                                 | 138 ms: 1.05x faster                                                        |
| logging_silent            | 102 ns                                                 | 97.3 ns: 1.05x faster                                                       |
| thrift                    | 809 us                                                 | 780 us: 1.04x faster                                                        |
| regex_effbot              | 3.73 ms                                                | 3.62 ms: 1.03x faster                                                       |
| async_tree_none_tg        | 321 ms                                                 | 311 ms: 1.03x faster                                                        |
| xml_etree_iterparse       | 101 ms                                                 | 98.7 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 563 ms: 1.03x faster                                                        |
| meteor_contest            | 109 ms                                                 | 106 ms: 1.02x faster                                                        |
| json_dumps                | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                       |
| pyflate                   | 471 ms                                                 | 462 ms: 1.02x faster                                                        |
| json                      | 5.36 ms                                                | 5.27 ms: 1.02x faster                                                       |
| regex_dna                 | 218 ms                                                 | 216 ms: 1.01x faster                                                        |
| typing_runtime_protocols  | 165 us                                                 | 163 us: 1.01x faster                                                        |
| pidigits                  | 186 ms                                                 | 185 ms: 1.01x faster                                                        |
| scimark_sor               | 124 ms                                                 | 124 ms: 1.00x slower                                                        |
| deltablue                 | 3.23 ms                                                | 3.24 ms: 1.01x slower                                                       |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                        |
| chaos                     | 58.1 ms                                                | 58.5 ms: 1.01x slower                                                       |
| pprint_pformat            | 1.49 sec                                               | 1.51 sec: 1.01x slower                                                      |
| pprint_safe_repr          | 728 ms                                                 | 738 ms: 1.01x slower                                                        |
| genshi_text               | 23.5 ms                                                | 23.9 ms: 1.01x slower                                                       |
| scimark_lu                | 113 ms                                                 | 115 ms: 1.02x slower                                                        |
| coroutines                | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                       |
| bench_thread_pool         | 822 us                                                 | 846 us: 1.03x slower                                                        |
| raytrace                  | 267 ms                                                 | 275 ms: 1.03x slower                                                        |
| python_startup_no_site    | 6.96 ms                                                | 7.17 ms: 1.03x slower                                                       |
| logging_simple            | 5.72 us                                                | 5.91 us: 1.03x slower                                                       |
| coverage                  | 84.0 ms                                                | 87.0 ms: 1.04x slower                                                       |
| json_loads                | 27.2 us                                                | 28.5 us: 1.05x slower                                                       |
| async_tree_io_tg          | 857 ms                                                 | 900 ms: 1.05x slower                                                        |
| async_generators          | 436 ms                                                 | 460 ms: 1.06x slower                                                        |
| pycparser                 | 1.20 sec                                               | 1.27 sec: 1.06x slower                                                      |
| 2to3                      | 267 ms                                                 | 285 ms: 1.07x slower                                                        |
| nqueens                   | 78.4 ms                                                | 83.8 ms: 1.07x slower                                                       |
| html5lib                  | 64.2 ms                                                | 69.1 ms: 1.08x slower                                                       |
| django_template           | 35.2 ms                                                | 37.9 ms: 1.08x slower                                                       |
| sqlglot_normalize         | 108 ms                                                 | 119 ms: 1.10x slower                                                        |
| async_tree_io             | 842 ms                                                 | 933 ms: 1.11x slower                                                        |
| hexiom                    | 6.16 ms                                                | 6.86 ms: 1.11x slower                                                       |
| tornado_http              | 92.4 ms                                                | 103 ms: 1.12x slower                                                        |
| sqlglot_optimize          | 53.7 ms                                                | 60.1 ms: 1.12x slower                                                       |
| sqlglot_transpile         | 1.58 ms                                                | 1.78 ms: 1.12x slower                                                       |
| regex_compile             | 132 ms                                                 | 151 ms: 1.14x slower                                                        |
| sympy_expand              | 463 ms                                                 | 530 ms: 1.14x slower                                                        |
| generators                | 29.0 ms                                                | 33.2 ms: 1.15x slower                                                       |
| dulwich_log               | 64.3 ms                                                | 74.1 ms: 1.15x slower                                                       |
| sympy_str                 | 275 ms                                                 | 319 ms: 1.16x slower                                                        |
| sqlglot_parse             | 1.27 ms                                                | 1.52 ms: 1.19x slower                                                       |
| genshi_xml                | 50.9 ms                                                | 63.5 ms: 1.25x slower                                                       |
| sympy_integrate           | 19.9 ms                                                | 24.9 ms: 1.25x slower                                                       |
| docutils                  | 2.59 sec                                               | 3.25 sec: 1.25x slower                                                      |
| sympy_sum                 | 150 ms                                                 | 189 ms: 1.26x slower                                                        |
| pylint                    | 313 ms                                                 | 416 ms: 1.33x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (6): pickle_pure_python, scimark_monte_carlo, comprehensions, async_tree_cpu_io_mixed_tg, bench_mp_pool, logging_format
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240906-3.14.0a0-7ad3776-JIT/bm-20240906-linux-x86_64-brandtbucher-underflow_known_dyna-3.14.0a0-7ad3776.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.010x faster
# HPT report

- Reliability score: 56.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x