# Results vs. 3.13.0

- fork: python
- ref: e256a7590a0149feadfe
- machine: windows-amd64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.017x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                     |
| html5lib       | 38.9 ms                                                     | 40.5 ms: 1.04x slower                                                      |
| tornado_http   | 93.0 ms                                                     | 83.1 ms: 1.12x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                       |
| async_tree_none            | 226 ms                                                      | 207 ms: 1.09x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 261 ms: 1.06x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 200 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 388 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 553 ms: 1.07x slower                                                       |
| async_tree_io              | 521 ms                                                      | 566 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.5 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.02x slower                                                       |
| float          | 49.9 ms                                                     | 55.2 ms: 1.10x slower                                                      |
| nbody          | 68.4 ms                                                     | 83.2 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.7 ms: 1.46x faster                                                      |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 90.4 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.6 ms                                                     | 92.5 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 63.9 ms: 1.03x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 57.7 ms: 1.07x slower                                                      |
| json_dumps           | 5.92 ms                                                     | 6.35 ms: 1.07x slower                                                      |
| xml_etree_process    | 37.0 ms                                                     | 40.9 ms: 1.10x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 212 us: 1.12x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.12x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.59 sec: 1.14x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 22.2 ms: 1.14x faster                                                      |
| python_startup_no_site | 18.1 ms                                                     | 18.4 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 6.81 ms: 1.07x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 17.0 ms: 1.09x slower                                                      |
| django_template | 22.4 ms                                                     | 24.8 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 523 us: 16.83x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 14.7 ms: 1.46x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 884 us: 1.42x faster                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 66.0 ms: 1.31x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.53 ms: 1.29x faster                                                      |
| deepcopy                   | 226 us                                                      | 193 us: 1.17x faster                                                       |
| async_tree_memoization_tg  | 288 ms                                                      | 251 ms: 1.15x faster                                                       |
| python_startup             | 25.4 ms                                                     | 22.2 ms: 1.14x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 20.8 us: 1.12x faster                                                      |
| tornado_http               | 93.0 ms                                                     | 83.1 ms: 1.12x faster                                                      |
| async_tree_none            | 226 ms                                                      | 207 ms: 1.09x faster                                                       |
| pathlib                    | 80.9 ms                                                     | 75.9 ms: 1.07x faster                                                      |
| deepcopy_reduce            | 2.06 us                                                     | 1.94 us: 1.06x faster                                                      |
| async_tree_memoization     | 276 ms                                                      | 261 ms: 1.06x faster                                                       |
| bench_thread_pool          | 847 us                                                      | 802 us: 1.06x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 200 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.6 ms                                                     | 92.5 ms: 1.01x faster                                                      |
| python_startup_no_site     | 18.1 ms                                                     | 18.4 ms: 1.02x slower                                                      |
| pidigits                   | 148 ms                                                      | 150 ms: 1.02x slower                                                       |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 388 ms: 1.03x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 89.7 ms: 1.03x slower                                                      |
| xml_etree_iterparse        | 61.8 ms                                                     | 63.9 ms: 1.03x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 110 us: 1.04x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.44 sec: 1.04x slower                                                     |
| html5lib                   | 38.9 ms                                                     | 40.5 ms: 1.04x slower                                                      |
| sympy_str                  | 169 ms                                                      | 176 ms: 1.05x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 42.8 ms: 1.05x slower                                                      |
| sympy_expand               | 291 ms                                                      | 306 ms: 1.05x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 47.8 ms: 1.05x slower                                                      |
| telco                      | 4.79 ms                                                     | 5.09 ms: 1.06x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.35 us: 1.07x slower                                                      |
| async_tree_io_tg           | 518 ms                                                      | 553 ms: 1.07x slower                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 57.7 ms: 1.07x slower                                                      |
| meteor_contest             | 73.5 ms                                                     | 78.6 ms: 1.07x slower                                                      |
| mako                       | 6.35 ms                                                     | 6.81 ms: 1.07x slower                                                      |
| json_dumps                 | 5.92 ms                                                     | 6.35 ms: 1.07x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.0 ms: 1.08x slower                                                      |
| coverage                   | 45.6 ms                                                     | 49.3 ms: 1.08x slower                                                      |
| pycparser                  | 683 ms                                                      | 740 ms: 1.08x slower                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.66 ms: 1.09x slower                                                      |
| async_tree_io              | 521 ms                                                      | 566 ms: 1.09x slower                                                       |
| docutils                   | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                     |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.85 us: 1.09x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 17.0 ms: 1.09x slower                                                      |
| pprint_safe_repr           | 494 ms                                                      | 542 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 36.3 ms: 1.10x slower                                                      |
| xml_etree_process          | 37.0 ms                                                     | 40.9 ms: 1.10x slower                                                      |
| float                      | 49.9 ms                                                     | 55.2 ms: 1.10x slower                                                      |
| sqlglot_normalize          | 175 ms                                                      | 193 ms: 1.11x slower                                                       |
| chaos                      | 38.5 ms                                                     | 42.7 ms: 1.11x slower                                                      |
| django_template            | 22.4 ms                                                     | 24.8 ms: 1.11x slower                                                      |
| spectral_norm              | 62.8 ms                                                     | 69.8 ms: 1.11x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 212 us: 1.12x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.12x slower                                                       |
| pprint_pformat             | 999 ms                                                      | 1.12 sec: 1.12x slower                                                     |
| regex_compile              | 80.5 ms                                                     | 90.4 ms: 1.12x slower                                                      |
| hexiom                     | 3.89 ms                                                     | 4.39 ms: 1.13x slower                                                      |
| coroutines                 | 12.8 ms                                                     | 14.5 ms: 1.13x slower                                                      |
| pyflate                    | 283 ms                                                      | 322 ms: 1.14x slower                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.59 sec: 1.14x slower                                                     |
| sqlglot_parse              | 771 us                                                      | 888 us: 1.15x slower                                                       |
| comprehensions             | 10.3 us                                                     | 11.9 us: 1.16x slower                                                      |
| nqueens                    | 56.7 ms                                                     | 65.5 ms: 1.16x slower                                                      |
| sqlglot_transpile          | 956 us                                                      | 1.11 ms: 1.16x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 63.8 ns: 1.17x slower                                                      |
| fannkuch                   | 253 ms                                                      | 299 ms: 1.18x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 62.5 ms: 1.18x slower                                                      |
| richards_super             | 30.9 ms                                                     | 36.4 ms: 1.18x slower                                                      |
| richards                   | 27.3 ms                                                     | 32.3 ms: 1.18x slower                                                      |
| raytrace                   | 160 ms                                                      | 189 ms: 1.18x slower                                                       |
| scimark_fft                | 172 ms                                                      | 204 ms: 1.19x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.28 ms: 1.19x slower                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 49.0 ms: 1.20x slower                                                      |
| nbody                      | 68.4 ms                                                     | 83.2 ms: 1.22x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 93.1 ms: 1.22x slower                                                      |
| json                       | 3.19 ms                                                     | 4.50 ms: 1.41x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (7): json_loads, regex_effbot, go, genshi_xml, 2to3, async_tree_cpu_io_mixed, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.017x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown