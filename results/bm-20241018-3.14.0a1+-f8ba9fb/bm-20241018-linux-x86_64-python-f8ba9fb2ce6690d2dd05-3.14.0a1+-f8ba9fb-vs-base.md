# Results vs. base

- fork: python
- ref: f8ba9fb2ce6690d2dd05
- machine: linux-x86_64
- commit hash: f8ba9fb
- commit date: 2024-10-18
- overall geometric mean: 1.00x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241018-linux-x86_64-python-6d93690954daae9e9a36-3.14.0a1+-6d93690 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 254 ms: 1.00x slower                                                   |
| docutils       | 2.66 sec                                                               | 2.68 sec: 1.01x slower                                                 |
| html5lib       | 63.0 ms                                                                | 63.6 ms: 1.01x slower                                                  |
| tornado_http   | 89.7 ms                                                                | 90.2 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241018-linux-x86_64-python-6d93690954daae9e9a36-3.14.0a1+-6d93690 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_generators           | 433 ms                                                                 | 431 ms: 1.00x faster                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                                               | 1.80 sec: 1.00x slower                                                 |
| asyncio_tcp                | 480 ms                                                                 | 484 ms: 1.01x slower                                                   |
| coroutines                 | 23.0 ms                                                                | 23.2 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 555 ms                                                                 | 563 ms: 1.01x slower                                                   |
| async_tree_io_tg           | 960 ms                                                                 | 975 ms: 1.02x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (7): asyncio_websockets, async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241018-linux-x86_64-python-6d93690954daae9e9a36-3.14.0a1+-6d93690 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x faster                                                   |
| float          | 79.3 ms                                                                | 79.9 ms: 1.01x slower                                                  |
| nbody          | 91.2 ms                                                                | 93.0 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241018-linux-x86_64-python-6d93690954daae9e9a36-3.14.0a1+-6d93690 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                                | 25.1 ms: 1.01x faster                                                  |
| regex_compile  | 128 ms                                                                 | 130 ms: 1.02x slower                                                   |
| regex_dna      | 213 ms                                                                 | 218 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241018-linux-x86_64-python-6d93690954daae9e9a36-3.14.0a1+-6d93690 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|--------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_dict        | 35.2 us                                                                | 33.9 us: 1.04x faster                                                  |
| pickle             | 11.7 us                                                                | 11.5 us: 1.02x faster                                                  |
| unpickle           | 14.8 us                                                                | 14.6 us: 1.01x faster                                                  |
| xml_etree_parse    | 156 ms                                                                 | 155 ms: 1.01x faster                                                   |
| pickle_pure_python | 311 us                                                                 | 313 us: 1.01x slower                                                   |
| tomli_loads        | 2.10 sec                                                               | 2.12 sec: 1.01x slower                                                 |
| xml_etree_generate | 85.2 ms                                                                | 86.1 ms: 1.01x slower                                                  |
| unpickle_list      | 5.32 us                                                                | 5.57 us: 1.05x slower                                                  |
| pickle_list        | 4.86 us                                                                | 5.21 us: 1.07x slower                                                  |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (5): xml_etree_iterparse, json_dumps, unpickle_pure_python, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241018-linux-x86_64-python-6d93690954daae9e9a36-3.14.0a1+-6d93690 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.02 ms                                                                | 7.03 ms: 1.00x slower                                                  |
| python_startup         | 11.8 ms                                                                | 11.8 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241018-linux-x86_64-python-6d93690954daae9e9a36-3.14.0a1+-6d93690 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                                | 33.8 ms: 1.02x faster                                                  |
| genshi_text     | 22.8 ms                                                                | 23.2 ms: 1.02x slower                                                  |
| mako            | 11.5 ms                                                                | 11.7 ms: 1.02x slower                                                  |
| genshi_xml      | 49.9 ms                                                                | 51.2 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241018-linux-x86_64-python-6d93690954daae9e9a36-3.14.0a1+-6d93690 | bm-20241018-linux-x86_64-python-f8ba9fb2ce6690d2dd05-3.14.0a1+-f8ba9fb |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpack_sequence            | 51.6 ns                                                                | 44.6 ns: 1.16x faster                                                  |
| pickle_dict                | 35.2 us                                                                | 33.9 us: 1.04x faster                                                  |
| thrift                     | 795 us                                                                 | 775 us: 1.03x faster                                                   |
| richards                   | 46.8 ms                                                                | 45.7 ms: 1.02x faster                                                  |
| django_template            | 34.6 ms                                                                | 33.8 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 742 ms                                                                 | 729 ms: 1.02x faster                                                   |
| pickle                     | 11.7 us                                                                | 11.5 us: 1.02x faster                                                  |
| richards_super             | 52.7 ms                                                                | 52.0 ms: 1.01x faster                                                  |
| gc_traversal               | 4.80 ms                                                                | 4.73 ms: 1.01x faster                                                  |
| unpickle                   | 14.8 us                                                                | 14.6 us: 1.01x faster                                                  |
| pathlib                    | 16.1 ms                                                                | 15.9 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.50 sec                                                               | 1.49 sec: 1.01x faster                                                 |
| regex_v8                   | 25.3 ms                                                                | 25.1 ms: 1.01x faster                                                  |
| comprehensions             | 16.8 us                                                                | 16.7 us: 1.01x faster                                                  |
| sqlglot_transpile          | 1.59 ms                                                                | 1.58 ms: 1.01x faster                                                  |
| meteor_contest             | 108 ms                                                                 | 107 ms: 1.01x faster                                                   |
| xml_etree_parse            | 156 ms                                                                 | 155 ms: 1.01x faster                                                   |
| async_generators           | 433 ms                                                                 | 431 ms: 1.00x faster                                                   |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x faster                                                   |
| python_startup_no_site     | 7.02 ms                                                                | 7.03 ms: 1.00x slower                                                  |
| python_startup             | 11.8 ms                                                                | 11.8 ms: 1.00x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                                               | 1.80 sec: 1.00x slower                                                 |
| 2to3                       | 254 ms                                                                 | 254 ms: 1.00x slower                                                   |
| create_gc_cycles           | 2.69 ms                                                                | 2.70 ms: 1.00x slower                                                  |
| sqlglot_optimize           | 53.0 ms                                                                | 53.2 ms: 1.00x slower                                                  |
| docutils                   | 2.66 sec                                                               | 2.68 sec: 1.01x slower                                                 |
| pickle_pure_python         | 311 us                                                                 | 313 us: 1.01x slower                                                   |
| tornado_http               | 89.7 ms                                                                | 90.2 ms: 1.01x slower                                                  |
| bench_thread_pool          | 841 us                                                                 | 846 us: 1.01x slower                                                   |
| nqueens                    | 81.2 ms                                                                | 81.7 ms: 1.01x slower                                                  |
| chaos                      | 60.6 ms                                                                | 61.0 ms: 1.01x slower                                                  |
| sympy_sum                  | 146 ms                                                                 | 147 ms: 1.01x slower                                                   |
| deepcopy_reduce            | 2.72 us                                                                | 2.74 us: 1.01x slower                                                  |
| tomli_loads                | 2.10 sec                                                               | 2.12 sec: 1.01x slower                                                 |
| float                      | 79.3 ms                                                                | 79.9 ms: 1.01x slower                                                  |
| asyncio_tcp                | 480 ms                                                                 | 484 ms: 1.01x slower                                                   |
| json                       | 4.83 ms                                                                | 4.87 ms: 1.01x slower                                                  |
| bpe_tokeniser              | 4.78 sec                                                               | 4.82 sec: 1.01x slower                                                 |
| deepcopy                   | 262 us                                                                 | 264 us: 1.01x slower                                                   |
| raytrace                   | 267 ms                                                                 | 270 ms: 1.01x slower                                                   |
| html5lib                   | 63.0 ms                                                                | 63.6 ms: 1.01x slower                                                  |
| scimark_lu                 | 115 ms                                                                 | 116 ms: 1.01x slower                                                   |
| sqlglot_normalize          | 105 ms                                                                 | 106 ms: 1.01x slower                                                   |
| xml_etree_generate         | 85.2 ms                                                                | 86.1 ms: 1.01x slower                                                  |
| coroutines                 | 23.0 ms                                                                | 23.2 ms: 1.01x slower                                                  |
| typing_runtime_protocols   | 161 us                                                                 | 163 us: 1.01x slower                                                   |
| hexiom                     | 6.28 ms                                                                | 6.37 ms: 1.01x slower                                                  |
| coverage                   | 83.6 ms                                                                | 84.8 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 555 ms                                                                 | 563 ms: 1.01x slower                                                   |
| regex_compile              | 128 ms                                                                 | 130 ms: 1.02x slower                                                   |
| async_tree_io_tg           | 960 ms                                                                 | 975 ms: 1.02x slower                                                   |
| logging_simple             | 5.48 us                                                                | 5.57 us: 1.02x slower                                                  |
| fannkuch                   | 407 ms                                                                 | 414 ms: 1.02x slower                                                   |
| generators                 | 27.4 ms                                                                | 27.8 ms: 1.02x slower                                                  |
| genshi_text                | 22.8 ms                                                                | 23.2 ms: 1.02x slower                                                  |
| mako                       | 11.5 ms                                                                | 11.7 ms: 1.02x slower                                                  |
| nbody                      | 91.2 ms                                                                | 93.0 ms: 1.02x slower                                                  |
| scimark_fft                | 367 ms                                                                 | 374 ms: 1.02x slower                                                   |
| regex_dna                  | 213 ms                                                                 | 218 ms: 1.02x slower                                                   |
| sqlite_synth               | 2.84 us                                                                | 2.91 us: 1.03x slower                                                  |
| genshi_xml                 | 49.9 ms                                                                | 51.2 ms: 1.03x slower                                                  |
| logging_format             | 6.04 us                                                                | 6.21 us: 1.03x slower                                                  |
| mdp                        | 2.56 sec                                                               | 2.63 sec: 1.03x slower                                                 |
| scimark_sparse_mat_mult    | 4.89 ms                                                                | 5.05 ms: 1.03x slower                                                  |
| crypto_pyaes               | 71.3 ms                                                                | 73.8 ms: 1.03x slower                                                  |
| pycparser                  | 1.13 sec                                                               | 1.17 sec: 1.04x slower                                                 |
| unpickle_list              | 5.32 us                                                                | 5.57 us: 1.05x slower                                                  |
| spectral_norm              | 111 ms                                                                 | 118 ms: 1.06x slower                                                   |
| pickle_list                | 4.86 us                                                                | 5.21 us: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (29): logging_silent, xml_etree_iterparse, sympy_expand, pyflate, go, sympy_str, dulwich_log, json_dumps, deepcopy_memo, unpickle_pure_python, sphinx, regex_effbot, asyncio_websockets, pylint, sympy_integrate, scimark_sor, scimark_monte_carlo, sqlglot_parse, bench_mp_pool, json_loads, xml_etree_process, telco, async_tree_none_tg, deltablue, async_tree_memoization_tg, async_tree_io, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x