# Results vs. 3.13.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-amd64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.018x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 227 ms: 1.03x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.9 ms                                                     | 39.9 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 260 ms: 1.06x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 199 ms: 1.05x faster                                                       |
| async_tree_none            | 226 ms                                                      | 217 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 390 ms: 1.03x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 541 ms: 1.04x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| async_tree_io              | 521 ms                                                      | 613 ms: 1.18x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 152 ms: 1.03x slower                                                       |
| float          | 49.9 ms                                                     | 57.2 ms: 1.15x slower                                                      |
| nbody          | 68.4 ms                                                     | 84.6 ms: 1.24x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.1 ms: 1.42x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 90.8 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| xml_etree_parse      | 93.6 ms                                                     | 94.3 ms: 1.01x slower                                                      |
| json_dumps           | 5.92 ms                                                     | 6.21 ms: 1.05x slower                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 65.3 ms: 1.06x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 58.4 ms: 1.08x slower                                                      |
| xml_etree_process    | 37.0 ms                                                     | 41.2 ms: 1.11x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 213 us: 1.12x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.12x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.60 sec: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.3 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 6.85 ms: 1.08x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| django_template | 22.4 ms                                                     | 24.9 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 515 us: 17.08x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 15.1 ms: 1.42x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 902 us: 1.40x faster                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 67.8 ms: 1.27x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.55 ms: 1.27x faster                                                      |
| deepcopy                   | 226 us                                                      | 189 us: 1.20x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 20.3 us: 1.15x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 253 ms: 1.14x faster                                                       |
| python_startup             | 25.4 ms                                                     | 22.3 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.06 us                                                     | 1.89 us: 1.09x faster                                                      |
| async_tree_memoization     | 276 ms                                                      | 260 ms: 1.06x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                      |
| async_tree_none_tg         | 209 ms                                                      | 199 ms: 1.05x faster                                                       |
| async_tree_none            | 226 ms                                                      | 217 ms: 1.04x faster                                                       |
| pathlib                    | 80.9 ms                                                     | 79.4 ms: 1.02x faster                                                      |
| xml_etree_parse            | 93.6 ms                                                     | 94.3 ms: 1.01x slower                                                      |
| html5lib                   | 38.9 ms                                                     | 39.9 ms: 1.02x slower                                                      |
| 2to3                       | 221 ms                                                      | 227 ms: 1.03x slower                                                       |
| pidigits                   | 148 ms                                                      | 152 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 390 ms: 1.03x slower                                                       |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 541 ms: 1.04x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.23 us: 1.05x slower                                                      |
| sympy_sum                  | 86.9 ms                                                     | 91.1 ms: 1.05x slower                                                      |
| sympy_str                  | 169 ms                                                      | 177 ms: 1.05x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 13.1 ms: 1.05x slower                                                      |
| json_dumps                 | 5.92 ms                                                     | 6.21 ms: 1.05x slower                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 47.8 ms: 1.05x slower                                                      |
| sympy_expand               | 291 ms                                                      | 307 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 65.3 ms: 1.06x slower                                                      |
| mdp                        | 1.39 sec                                                    | 1.47 sec: 1.06x slower                                                     |
| logging_format             | 6.26 us                                                     | 6.64 us: 1.06x slower                                                      |
| coverage                   | 45.6 ms                                                     | 48.6 ms: 1.07x slower                                                      |
| telco                      | 4.79 ms                                                     | 5.12 ms: 1.07x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 113 us: 1.07x slower                                                       |
| generators                 | 19.5 ms                                                     | 20.9 ms: 1.07x slower                                                      |
| meteor_contest             | 73.5 ms                                                     | 79.0 ms: 1.07x slower                                                      |
| mako                       | 6.35 ms                                                     | 6.85 ms: 1.08x slower                                                      |
| dulwich_log                | 40.8 ms                                                     | 44.1 ms: 1.08x slower                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 58.4 ms: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| sqlglot_normalize          | 175 ms                                                      | 190 ms: 1.09x slower                                                       |
| genshi_text                | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| spectral_norm              | 62.8 ms                                                     | 69.0 ms: 1.10x slower                                                      |
| sqlglot_optimize           | 32.9 ms                                                     | 36.2 ms: 1.10x slower                                                      |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.11x slower                                                      |
| xml_etree_process          | 37.0 ms                                                     | 41.2 ms: 1.11x slower                                                      |
| pprint_safe_repr           | 494 ms                                                      | 549 ms: 1.11x slower                                                       |
| django_template            | 22.4 ms                                                     | 24.9 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| chaos                      | 38.5 ms                                                     | 43.0 ms: 1.12x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.12 sec: 1.12x slower                                                     |
| pycparser                  | 683 ms                                                      | 767 ms: 1.12x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 213 us: 1.12x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.12x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 63.8 ms: 1.13x slower                                                      |
| regex_compile              | 80.5 ms                                                     | 90.8 ms: 1.13x slower                                                      |
| pyflate                    | 283 ms                                                      | 321 ms: 1.13x slower                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.79 ms: 1.14x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 62.5 ns: 1.14x slower                                                      |
| float                      | 49.9 ms                                                     | 57.2 ms: 1.15x slower                                                      |
| fannkuch                   | 253 ms                                                      | 291 ms: 1.15x slower                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.60 sec: 1.15x slower                                                     |
| sqlglot_transpile          | 956 us                                                      | 1.10 ms: 1.15x slower                                                      |
| comprehensions             | 10.3 us                                                     | 11.9 us: 1.15x slower                                                      |
| hexiom                     | 3.89 ms                                                     | 4.50 ms: 1.16x slower                                                      |
| sqlglot_parse              | 771 us                                                      | 892 us: 1.16x slower                                                       |
| richards_super             | 30.9 ms                                                     | 36.1 ms: 1.17x slower                                                      |
| async_tree_io              | 521 ms                                                      | 613 ms: 1.18x slower                                                       |
| richards                   | 27.3 ms                                                     | 32.1 ms: 1.18x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.26 ms: 1.18x slower                                                      |
| scimark_fft                | 172 ms                                                      | 205 ms: 1.19x slower                                                       |
| raytrace                   | 160 ms                                                      | 191 ms: 1.19x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 91.5 ms: 1.20x slower                                                      |
| scimark_lu                 | 53.0 ms                                                     | 64.7 ms: 1.22x slower                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 50.4 ms: 1.24x slower                                                      |
| nbody                      | 68.4 ms                                                     | 84.6 ms: 1.24x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (9): bench_thread_pool, json, python_startup_no_site, go, async_tree_cpu_io_mixed, regex_effbot, tornado_http, genshi_xml, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1-amd64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.018x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown