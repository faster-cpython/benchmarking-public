# Results vs. 3.13.0

- fork: python
- ref: b3aa1b5fe260382788a2
- machine: windows-amd64
- commit hash: b3aa1b5
- commit date: 2024-10-11
- overall geometric mean: 1.025x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 229 ms: 1.03x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.72 sec: 1.10x slower                                                     |
| html5lib       | 38.9 ms                                                     | 42.9 ms: 1.10x slower                                                      |
| tornado_http   | 93.0 ms                                                     | 94.9 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 258 ms: 1.12x faster                                                       |
| async_tree_none            | 226 ms                                                      | 214 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 396 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 391 ms: 1.04x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                                      |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 579 ms: 1.12x slower                                                       |
| async_tree_io              | 521 ms                                                      | 591 ms: 1.13x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| float          | 49.9 ms                                                     | 53.8 ms: 1.08x slower                                                      |
| nbody          | 68.4 ms                                                     | 79.3 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.3 ms: 1.40x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 91.3 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.7 us: 1.03x faster                                                      |
| xml_etree_parse      | 93.6 ms                                                     | 96.5 ms: 1.03x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 57.4 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 66.3 ms: 1.07x slower                                                      |
| xml_etree_process    | 37.0 ms                                                     | 40.2 ms: 1.08x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                       |
| json_dumps           | 5.92 ms                                                     | 6.75 ms: 1.14x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 220 us: 1.16x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.64 sec: 1.17x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.3 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 37.0 ms: 1.04x slower                                                      |
| mako            | 6.35 ms                                                     | 6.78 ms: 1.07x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| django_template | 22.4 ms                                                     | 25.7 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 516 us: 17.05x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 15.3 ms: 1.40x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 923 us: 1.36x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.53 ms: 1.28x faster                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 69.3 ms: 1.25x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 19.7 us: 1.18x faster                                                      |
| deepcopy                   | 226 us                                                      | 193 us: 1.17x faster                                                       |
| python_startup             | 25.4 ms                                                     | 22.3 ms: 1.14x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 258 ms: 1.12x faster                                                       |
| async_tree_none            | 226 ms                                                      | 214 ms: 1.05x faster                                                       |
| bench_thread_pool          | 847 us                                                      | 812 us: 1.04x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 2.00 us: 1.03x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.7 us: 1.03x faster                                                      |
| pathlib                    | 80.9 ms                                                     | 80.4 ms: 1.01x faster                                                      |
| go                         | 87.0 ms                                                     | 86.4 ms: 1.01x faster                                                      |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| telco                      | 4.79 ms                                                     | 4.83 ms: 1.01x slower                                                      |
| tornado_http               | 93.0 ms                                                     | 94.9 ms: 1.02x slower                                                      |
| coverage                   | 45.6 ms                                                     | 46.6 ms: 1.02x slower                                                      |
| xml_etree_parse            | 93.6 ms                                                     | 96.5 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 396 ms: 1.03x slower                                                       |
| 2to3                       | 221 ms                                                      | 229 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 391 ms: 1.04x slower                                                       |
| meteor_contest             | 73.5 ms                                                     | 76.6 ms: 1.04x slower                                                      |
| genshi_xml                 | 35.5 ms                                                     | 37.0 ms: 1.04x slower                                                      |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 90.9 ms: 1.05x slower                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 48.1 ms: 1.06x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 112 us: 1.06x slower                                                       |
| sympy_str                  | 169 ms                                                      | 178 ms: 1.06x slower                                                       |
| sympy_expand               | 291 ms                                                      | 309 ms: 1.06x slower                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 57.4 ms: 1.06x slower                                                      |
| mako                       | 6.35 ms                                                     | 6.78 ms: 1.07x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.38 us: 1.07x slower                                                      |
| xml_etree_iterparse        | 61.8 ms                                                     | 66.3 ms: 1.07x slower                                                      |
| float                      | 49.9 ms                                                     | 53.8 ms: 1.08x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                      |
| coroutines                 | 12.8 ms                                                     | 13.8 ms: 1.08x slower                                                      |
| xml_etree_process          | 37.0 ms                                                     | 40.2 ms: 1.08x slower                                                      |
| spectral_norm              | 62.8 ms                                                     | 68.3 ms: 1.09x slower                                                      |
| pycparser                  | 683 ms                                                      | 743 ms: 1.09x slower                                                       |
| dulwich_log                | 40.8 ms                                                     | 44.5 ms: 1.09x slower                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.68 ms: 1.09x slower                                                      |
| pylint                     | 211 ms                                                      | 230 ms: 1.09x slower                                                       |
| logging_format             | 6.26 us                                                     | 6.85 us: 1.09x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.72 sec: 1.10x slower                                                     |
| genshi_text                | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| html5lib                   | 38.9 ms                                                     | 42.9 ms: 1.10x slower                                                      |
| scimark_lu                 | 53.0 ms                                                     | 58.4 ms: 1.10x slower                                                      |
| generators                 | 19.5 ms                                                     | 21.5 ms: 1.10x slower                                                      |
| pprint_safe_repr           | 494 ms                                                      | 547 ms: 1.11x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 60.7 ns: 1.11x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                       |
| hexiom                     | 3.89 ms                                                     | 4.33 ms: 1.11x slower                                                      |
| fannkuch                   | 253 ms                                                      | 282 ms: 1.11x slower                                                       |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 579 ms: 1.12x slower                                                       |
| mdp                        | 1.39 sec                                                    | 1.55 sec: 1.12x slower                                                     |
| pprint_pformat             | 999 ms                                                      | 1.12 sec: 1.12x slower                                                     |
| sqlglot_normalize          | 175 ms                                                      | 196 ms: 1.12x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 36.9 ms: 1.12x slower                                                      |
| pyflate                    | 283 ms                                                      | 318 ms: 1.12x slower                                                       |
| async_tree_io              | 521 ms                                                      | 591 ms: 1.13x slower                                                       |
| regex_compile              | 80.5 ms                                                     | 91.3 ms: 1.13x slower                                                      |
| chaos                      | 38.5 ms                                                     | 43.7 ms: 1.13x slower                                                      |
| nqueens                    | 56.7 ms                                                     | 64.4 ms: 1.14x slower                                                      |
| json_dumps                 | 5.92 ms                                                     | 6.75 ms: 1.14x slower                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 46.7 ms: 1.14x slower                                                      |
| django_template            | 22.4 ms                                                     | 25.7 ms: 1.15x slower                                                      |
| comprehensions             | 10.3 us                                                     | 11.8 us: 1.15x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 88.2 ms: 1.16x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 220 us: 1.16x slower                                                       |
| nbody                      | 68.4 ms                                                     | 79.3 ms: 1.16x slower                                                      |
| tomli_loads                | 1.39 sec                                                    | 1.64 sec: 1.17x slower                                                     |
| richards_super             | 30.9 ms                                                     | 36.2 ms: 1.17x slower                                                      |
| richards                   | 27.3 ms                                                     | 32.1 ms: 1.17x slower                                                      |
| sqlglot_parse              | 771 us                                                      | 908 us: 1.18x slower                                                       |
| deltablue                  | 1.92 ms                                                     | 2.26 ms: 1.18x slower                                                      |
| scimark_fft                | 172 ms                                                      | 203 ms: 1.18x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.14 ms: 1.19x slower                                                      |
| raytrace                   | 160 ms                                                      | 207 ms: 1.30x slower                                                       |
| json                       | 3.19 ms                                                     | 4.18 ms: 1.31x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_none_tg, regex_effbot, python_startup_no_site
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241011-3.14.0a0-b3aa1b5/bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.025x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown