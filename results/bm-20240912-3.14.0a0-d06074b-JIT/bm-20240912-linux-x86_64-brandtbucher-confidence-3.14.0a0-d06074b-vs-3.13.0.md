# Results vs. 3.13.0

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: d06074b
- commit date: 2024-09-12
- overall geometric mean: 1.037x faster
- HPT reliability: 97.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 273 ms: 1.02x slower                                              |
| docutils       | 2.59 sec                                               | 2.96 sec: 1.14x slower                                            |
| html5lib       | 64.2 ms                                                | 64.6 ms: 1.01x slower                                             |
| tornado_http   | 92.4 ms                                                | 94.9 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                  | 1.05x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 384 ms: 1.21x faster                                              |
| async_tree_memoization     | 442 ms                                                 | 393 ms: 1.12x faster                                              |
| async_tree_none            | 351 ms                                                 | 315 ms: 1.11x faster                                              |
| async_tree_none_tg         | 321 ms                                                 | 303 ms: 1.06x faster                                              |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 568 ms: 1.02x faster                                              |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 552 ms: 1.01x slower                                              |
| async_tree_io_tg           | 857 ms                                                 | 873 ms: 1.02x slower                                              |
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                              |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (2): coroutines, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.9 ms: 1.13x faster                                             |
| nbody          | 87.0 ms                                                | 79.9 ms: 1.09x faster                                             |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.4 ms: 1.07x faster                                             |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                              |
| regex_effbot   | 3.73 ms                                                | 3.82 ms: 1.02x slower                                             |
| regex_compile  | 132 ms                                                 | 140 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|---------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_generate  | 86.7 ms                                                | 76.9 ms: 1.13x faster                                             |
| xml_etree_process   | 60.6 ms                                                | 54.6 ms: 1.11x faster                                             |
| tomli_loads         | 2.14 sec                                               | 1.94 sec: 1.10x faster                                            |
| xml_etree_parse     | 156 ms                                                 | 145 ms: 1.07x faster                                              |
| json_dumps          | 10.6 ms                                                | 10.1 ms: 1.05x faster                                             |
| xml_etree_iterparse | 101 ms                                                 | 98.3 ms: 1.03x faster                                             |
| pickle_pure_python  | 310 us                                                 | 304 us: 1.02x faster                                              |
| json_loads          | 27.2 us                                                | 27.0 us: 1.01x faster                                             |
| Geometric mean      | (ref)                                                  | 1.06x faster                                                      |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                             |
| python_startup_no_site | 6.96 ms                                                | 7.04 ms: 1.01x slower                                             |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.85 ms: 1.13x faster                                             |
| django_template | 35.2 ms                                                | 35.9 ms: 1.02x slower                                             |
| genshi_text     | 23.5 ms                                                | 24.8 ms: 1.05x slower                                             |
| genshi_xml      | 50.9 ms                                                | 56.4 ms: 1.11x slower                                             |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 27.0 us: 1.45x faster                                             |
| deepcopy                   | 358 us                                                 | 259 us: 1.38x faster                                              |
| create_gc_cycles           | 2.41 ms                                                | 1.75 ms: 1.38x faster                                             |
| richards_super             | 54.9 ms                                                | 43.3 ms: 1.27x faster                                             |
| richards                   | 48.7 ms                                                | 39.3 ms: 1.24x faster                                             |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.11 ms: 1.23x faster                                             |
| deepcopy_reduce            | 3.20 us                                                | 2.64 us: 1.21x faster                                             |
| async_tree_memoization_tg  | 464 ms                                                 | 384 ms: 1.21x faster                                              |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                             |
| scimark_fft                | 364 ms                                                 | 308 ms: 1.18x faster                                              |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.15x faster                                              |
| crypto_pyaes               | 75.3 ms                                                | 66.0 ms: 1.14x faster                                             |
| float                      | 79.2 ms                                                | 69.9 ms: 1.13x faster                                             |
| xml_etree_generate         | 86.7 ms                                                | 76.9 ms: 1.13x faster                                             |
| mako                       | 11.1 ms                                                | 9.85 ms: 1.13x faster                                             |
| async_tree_memoization     | 442 ms                                                 | 393 ms: 1.12x faster                                              |
| async_tree_none            | 351 ms                                                 | 315 ms: 1.11x faster                                              |
| xml_etree_process          | 60.6 ms                                                | 54.6 ms: 1.11x faster                                             |
| tomli_loads                | 2.14 sec                                               | 1.94 sec: 1.10x faster                                            |
| pathlib                    | 17.5 ms                                                | 15.9 ms: 1.10x faster                                             |
| go                         | 144 ms                                                 | 131 ms: 1.10x faster                                              |
| gc_traversal               | 4.37 ms                                                | 3.98 ms: 1.10x faster                                             |
| pyflate                    | 471 ms                                                 | 430 ms: 1.09x faster                                              |
| nbody                      | 87.0 ms                                                | 79.9 ms: 1.09x faster                                             |
| scimark_monte_carlo        | 67.4 ms                                                | 62.3 ms: 1.08x faster                                             |
| fannkuch                   | 404 ms                                                 | 375 ms: 1.08x faster                                              |
| regex_v8                   | 26.2 ms                                                | 24.4 ms: 1.07x faster                                             |
| bpe_tokeniser              | 4.75 sec                                               | 4.43 sec: 1.07x faster                                            |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.07x faster                                              |
| json                       | 5.36 ms                                                | 5.01 ms: 1.07x faster                                             |
| telco                      | 8.54 ms                                                | 8.00 ms: 1.07x faster                                             |
| scimark_sor                | 124 ms                                                 | 116 ms: 1.06x faster                                              |
| async_tree_none_tg         | 321 ms                                                 | 303 ms: 1.06x faster                                              |
| logging_format             | 6.40 us                                                | 6.11 us: 1.05x faster                                             |
| json_dumps                 | 10.6 ms                                                | 10.1 ms: 1.05x faster                                             |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                            |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.03x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 98.3 ms: 1.03x faster                                             |
| pprint_safe_repr           | 728 ms                                                 | 710 ms: 1.03x faster                                              |
| thrift                     | 809 us                                                 | 789 us: 1.03x faster                                              |
| mdp                        | 2.72 sec                                               | 2.66 sec: 1.02x faster                                            |
| pickle_pure_python         | 310 us                                                 | 304 us: 1.02x faster                                              |
| logging_simple             | 5.72 us                                                | 5.61 us: 1.02x faster                                             |
| scimark_lu                 | 113 ms                                                 | 111 ms: 1.02x faster                                              |
| pprint_pformat             | 1.49 sec                                               | 1.47 sec: 1.02x faster                                            |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 568 ms: 1.02x faster                                              |
| typing_runtime_protocols   | 165 us                                                 | 162 us: 1.01x faster                                              |
| json_loads                 | 27.2 us                                                | 27.0 us: 1.01x faster                                             |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                              |
| coverage                   | 84.0 ms                                                | 84.4 ms: 1.00x slower                                             |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                              |
| html5lib                   | 64.2 ms                                                | 64.6 ms: 1.01x slower                                             |
| python_startup_no_site     | 6.96 ms                                                | 7.04 ms: 1.01x slower                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 552 ms: 1.01x slower                                              |
| regex_dna                  | 218 ms                                                 | 221 ms: 1.01x slower                                              |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                             |
| async_tree_io_tg           | 857 ms                                                 | 873 ms: 1.02x slower                                              |
| chaos                      | 58.1 ms                                                | 59.2 ms: 1.02x slower                                             |
| django_template            | 35.2 ms                                                | 35.9 ms: 1.02x slower                                             |
| bench_thread_pool          | 822 us                                                 | 838 us: 1.02x slower                                              |
| 2to3                       | 267 ms                                                 | 273 ms: 1.02x slower                                              |
| regex_effbot               | 3.73 ms                                                | 3.82 ms: 1.02x slower                                             |
| tornado_http               | 92.4 ms                                                | 94.9 ms: 1.03x slower                                             |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                              |
| raytrace                   | 267 ms                                                 | 276 ms: 1.03x slower                                              |
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                              |
| dulwich_log                | 64.3 ms                                                | 67.3 ms: 1.05x slower                                             |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                              |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.05x slower                                             |
| genshi_text                | 23.5 ms                                                | 24.8 ms: 1.05x slower                                             |
| regex_compile              | 132 ms                                                 | 140 ms: 1.06x slower                                              |
| sqlglot_transpile          | 1.58 ms                                                | 1.68 ms: 1.06x slower                                             |
| nqueens                    | 78.4 ms                                                | 84.1 ms: 1.07x slower                                             |
| sympy_expand               | 463 ms                                                 | 500 ms: 1.08x slower                                              |
| sqlglot_optimize           | 53.7 ms                                                | 58.2 ms: 1.08x slower                                             |
| sympy_str                  | 275 ms                                                 | 298 ms: 1.09x slower                                              |
| genshi_xml                 | 50.9 ms                                                | 56.4 ms: 1.11x slower                                             |
| hexiom                     | 6.16 ms                                                | 6.88 ms: 1.12x slower                                             |
| generators                 | 29.0 ms                                                | 32.9 ms: 1.13x slower                                             |
| docutils                   | 2.59 sec                                               | 2.96 sec: 1.14x slower                                            |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.14x slower                                              |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.14x slower                                             |
| pylint                     | 313 ms                                                 | 375 ms: 1.20x slower                                              |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (5): coroutines, bench_mp_pool, unpickle_pure_python, deltablue, async_tree_io
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240912-3.14.0a0-d06074b-JIT/bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 97.97% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x