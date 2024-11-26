# Results vs. 3.13.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-x86_64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.037x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 253 ms: 1.05x faster                                                  |
| docutils       | 2.59 sec                                               | 2.66 sec: 1.03x slower                                                |
| html5lib       | 64.2 ms                                                | 62.4 ms: 1.03x faster                                                 |
| tornado_http   | 92.4 ms                                                | 89.9 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 391 ms: 1.19x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                                  |
| async_tree_none            | 351 ms                                                 | 315 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                                  |
| asyncio_websockets         | 552 ms                                                 | 559 ms: 1.01x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 875 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 558 ms: 1.02x slower                                                  |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                 |
| async_tree_io              | 842 ms                                                 | 873 ms: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (2): async_tree_none_tg, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.7 ms: 1.03x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| nbody          | 87.0 ms                                                | 89.5 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.6 ms: 1.06x faster                                                 |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                  |
| regex_effbot   | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                 |
| regex_dna      | 218 ms                                                 | 216 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.04 sec: 1.05x faster                                                |
| pickle_pure_python   | 310 us                                                 | 302 us: 1.03x faster                                                  |
| xml_etree_process    | 60.6 ms                                                | 59.0 ms: 1.03x faster                                                 |
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                 |
| xml_etree_generate   | 86.7 ms                                                | 85.4 ms: 1.02x faster                                                 |
| unpickle_pure_python | 216 us                                                 | 213 us: 1.01x faster                                                  |
| json_loads           | 27.2 us                                                | 27.0 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 105 ms: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 6.99 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 21.7 ms: 1.09x faster                                                 |
| genshi_xml      | 50.9 ms                                                | 48.6 ms: 1.05x faster                                                 |
| django_template | 35.2 ms                                                | 34.6 ms: 1.02x faster                                                 |
| mako            | 11.1 ms                                                | 11.1 ms: 1.00x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 255 us: 1.40x faster                                                  |
| create_gc_cycles           | 2.41 ms                                                | 1.73 ms: 1.39x faster                                                 |
| deepcopy_memo              | 39.1 us                                                | 29.5 us: 1.32x faster                                                 |
| go                         | 144 ms                                                 | 117 ms: 1.23x faster                                                  |
| deepcopy_reduce            | 3.20 us                                                | 2.63 us: 1.22x faster                                                 |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                 |
| async_tree_memoization_tg  | 464 ms                                                 | 391 ms: 1.19x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 395 ms: 1.12x faster                                                  |
| gc_traversal               | 4.37 ms                                                | 3.90 ms: 1.12x faster                                                 |
| async_tree_none            | 351 ms                                                 | 315 ms: 1.11x faster                                                  |
| pathlib                    | 17.5 ms                                                | 15.9 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.60 ms: 1.10x faster                                                 |
| genshi_text                | 23.5 ms                                                | 21.7 ms: 1.09x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                |
| regex_v8                   | 26.2 ms                                                | 24.6 ms: 1.06x faster                                                 |
| richards                   | 48.7 ms                                                | 45.8 ms: 1.06x faster                                                 |
| richards_super             | 54.9 ms                                                | 51.7 ms: 1.06x faster                                                 |
| crypto_pyaes               | 75.3 ms                                                | 71.1 ms: 1.06x faster                                                 |
| 2to3                       | 267 ms                                                 | 253 ms: 1.05x faster                                                  |
| genshi_xml                 | 50.9 ms                                                | 48.6 ms: 1.05x faster                                                 |
| tomli_loads                | 2.14 sec                                               | 2.04 sec: 1.05x faster                                                |
| bench_thread_pool          | 822 us                                                 | 787 us: 1.04x faster                                                  |
| logging_format             | 6.40 us                                                | 6.12 us: 1.04x faster                                                 |
| typing_runtime_protocols   | 165 us                                                 | 158 us: 1.04x faster                                                  |
| json                       | 5.36 ms                                                | 5.15 ms: 1.04x faster                                                 |
| logging_simple             | 5.72 us                                                | 5.49 us: 1.04x faster                                                 |
| thrift                     | 809 us                                                 | 779 us: 1.04x faster                                                  |
| float                      | 79.2 ms                                                | 76.7 ms: 1.03x faster                                                 |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                  |
| sympy_str                  | 275 ms                                                 | 267 ms: 1.03x faster                                                  |
| pickle_pure_python         | 310 us                                                 | 302 us: 1.03x faster                                                  |
| html5lib                   | 64.2 ms                                                | 62.4 ms: 1.03x faster                                                 |
| tornado_http               | 92.4 ms                                                | 89.9 ms: 1.03x faster                                                 |
| xml_etree_process          | 60.6 ms                                                | 59.0 ms: 1.03x faster                                                 |
| generators                 | 29.0 ms                                                | 28.2 ms: 1.03x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.03x faster                                                  |
| deltablue                  | 3.23 ms                                                | 3.14 ms: 1.03x faster                                                 |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| json_dumps                 | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                 |
| regex_effbot               | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                 |
| sympy_integrate            | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                 |
| raytrace                   | 267 ms                                                 | 262 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 728 ms                                                 | 714 ms: 1.02x faster                                                  |
| logging_silent             | 102 ns                                                 | 99.9 ns: 1.02x faster                                                 |
| sympy_expand               | 463 ms                                                 | 456 ms: 1.02x faster                                                  |
| django_template            | 35.2 ms                                                | 34.6 ms: 1.02x faster                                                 |
| pprint_pformat             | 1.49 sec                                               | 1.47 sec: 1.02x faster                                                |
| xml_etree_generate         | 86.7 ms                                                | 85.4 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                                  |
| scimark_sor                | 124 ms                                                 | 122 ms: 1.01x faster                                                  |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                  |
| mdp                        | 2.72 sec                                               | 2.69 sec: 1.01x faster                                                |
| unpickle_pure_python       | 216 us                                                 | 213 us: 1.01x faster                                                  |
| sqlglot_optimize           | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                 |
| telco                      | 8.54 ms                                                | 8.46 ms: 1.01x faster                                                 |
| json_loads                 | 27.2 us                                                | 27.0 us: 1.01x faster                                                 |
| regex_dna                  | 218 ms                                                 | 216 ms: 1.01x faster                                                  |
| scimark_monte_carlo        | 67.4 ms                                                | 67.1 ms: 1.00x faster                                                 |
| sqlglot_transpile          | 1.58 ms                                                | 1.58 ms: 1.00x faster                                                 |
| scimark_fft                | 364 ms                                                 | 363 ms: 1.00x faster                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| mako                       | 11.1 ms                                                | 11.1 ms: 1.00x slower                                                 |
| python_startup_no_site     | 6.96 ms                                                | 6.99 ms: 1.00x slower                                                 |
| chaos                      | 58.1 ms                                                | 58.3 ms: 1.00x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                 |
| pyflate                    | 471 ms                                                 | 476 ms: 1.01x slower                                                  |
| asyncio_websockets         | 552 ms                                                 | 559 ms: 1.01x slower                                                  |
| coverage                   | 84.0 ms                                                | 85.7 ms: 1.02x slower                                                 |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                 |
| async_tree_io_tg           | 857 ms                                                 | 875 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 558 ms: 1.02x slower                                                  |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                 |
| bpe_tokeniser              | 4.75 sec                                               | 4.86 sec: 1.02x slower                                                |
| nqueens                    | 78.4 ms                                                | 80.4 ms: 1.03x slower                                                 |
| docutils                   | 2.59 sec                                               | 2.66 sec: 1.03x slower                                                |
| nbody                      | 87.0 ms                                                | 89.5 ms: 1.03x slower                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 105 ms: 1.04x slower                                                  |
| async_tree_io              | 842 ms                                                 | 873 ms: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (10): async_tree_none_tg, fannkuch, hexiom, xml_etree_parse, bench_mp_pool, scimark_lu, dulwich_log, sqlglot_normalize, async_generators, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.037x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x