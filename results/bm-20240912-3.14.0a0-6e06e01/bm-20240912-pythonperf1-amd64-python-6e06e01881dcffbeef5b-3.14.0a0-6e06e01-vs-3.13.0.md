# Results vs. 3.13.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: windows-amd64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.010x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 224 ms: 1.01x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| html5lib       | 38.9 ms                                                     | 40.3 ms: 1.03x slower                                                      |
| tornado_http   | 93.0 ms                                                     | 84.4 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.15x faster                                                       |
| async_tree_none            | 226 ms                                                      | 208 ms: 1.08x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 262 ms: 1.05x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 202 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 394 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 397 ms: 1.05x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 560 ms: 1.08x slower                                                       |
| async_tree_io              | 521 ms                                                      | 570 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.11x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| float          | 49.9 ms                                                     | 56.1 ms: 1.12x slower                                                      |
| nbody          | 68.4 ms                                                     | 83.7 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.6 ms: 1.46x faster                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 91.8 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| json_dumps           | 5.92 ms                                                     | 6.19 ms: 1.05x slower                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 64.9 ms: 1.05x slower                                                      |
| xml_etree_generate   | 54.0 ms                                                     | 57.9 ms: 1.07x slower                                                      |
| xml_etree_process    | 37.0 ms                                                     | 41.1 ms: 1.11x slower                                                      |
| pickle_pure_python   | 190 us                                                      | 210 us: 1.11x slower                                                       |
| tomli_loads          | 1.39 sec                                                    | 1.58 sec: 1.13x slower                                                     |
| unpickle_pure_python | 133 us                                                      | 151 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 21.7 ms: 1.17x faster                                                      |
| python_startup_no_site | 18.1 ms                                                     | 17.6 ms: 1.03x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 6.89 ms: 1.08x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| django_template | 22.4 ms                                                     | 26.0 ms: 1.16x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.09x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 523 us: 16.83x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 14.6 ms: 1.46x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 883 us: 1.42x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.53 ms: 1.29x faster                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 67.6 ms: 1.28x faster                                                      |
| deepcopy                   | 226 us                                                      | 189 us: 1.20x faster                                                       |
| python_startup             | 25.4 ms                                                     | 21.7 ms: 1.17x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 252 ms: 1.15x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 20.4 us: 1.14x faster                                                      |
| tornado_http               | 93.0 ms                                                     | 84.4 ms: 1.10x faster                                                      |
| async_tree_none            | 226 ms                                                      | 208 ms: 1.08x faster                                                       |
| pathlib                    | 80.9 ms                                                     | 75.6 ms: 1.07x faster                                                      |
| deepcopy_reduce            | 2.06 us                                                     | 1.93 us: 1.07x faster                                                      |
| async_tree_memoization     | 276 ms                                                      | 262 ms: 1.05x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| bench_thread_pool          | 847 us                                                      | 808 us: 1.05x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 202 ms: 1.04x faster                                                       |
| python_startup_no_site     | 18.1 ms                                                     | 17.6 ms: 1.03x faster                                                      |
| go                         | 87.0 ms                                                     | 85.8 ms: 1.01x faster                                                      |
| 2to3                       | 221 ms                                                      | 224 ms: 1.01x slower                                                       |
| pidigits                   | 148 ms                                                      | 150 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 394 ms: 1.03x slower                                                       |
| coverage                   | 45.6 ms                                                     | 46.9 ms: 1.03x slower                                                      |
| html5lib                   | 38.9 ms                                                     | 40.3 ms: 1.03x slower                                                      |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 90.0 ms: 1.04x slower                                                      |
| telco                      | 4.79 ms                                                     | 4.97 ms: 1.04x slower                                                      |
| mdp                        | 1.39 sec                                                    | 1.44 sec: 1.04x slower                                                     |
| json_dumps                 | 5.92 ms                                                     | 6.19 ms: 1.05x slower                                                      |
| dulwich_log                | 40.8 ms                                                     | 42.8 ms: 1.05x slower                                                      |
| sympy_str                  | 169 ms                                                      | 177 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 61.8 ms                                                     | 64.9 ms: 1.05x slower                                                      |
| sympy_expand               | 291 ms                                                      | 306 ms: 1.05x slower                                                       |
| crypto_pyaes               | 45.4 ms                                                     | 47.8 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 397 ms: 1.05x slower                                                       |
| sympy_integrate            | 12.5 ms                                                     | 13.2 ms: 1.06x slower                                                      |
| spectral_norm              | 62.8 ms                                                     | 66.4 ms: 1.06x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 113 us: 1.07x slower                                                       |
| xml_etree_generate         | 54.0 ms                                                     | 57.9 ms: 1.07x slower                                                      |
| meteor_contest             | 73.5 ms                                                     | 78.9 ms: 1.07x slower                                                      |
| logging_simple             | 5.96 us                                                     | 6.43 us: 1.08x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.70 sec: 1.08x slower                                                     |
| async_tree_io_tg           | 518 ms                                                      | 560 ms: 1.08x slower                                                       |
| mako                       | 6.35 ms                                                     | 6.89 ms: 1.08x slower                                                      |
| async_tree_io              | 521 ms                                                      | 570 ms: 1.09x slower                                                       |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.69 ms: 1.09x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| pprint_safe_repr           | 494 ms                                                      | 541 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 36.2 ms: 1.10x slower                                                      |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| generators                 | 19.5 ms                                                     | 21.5 ms: 1.10x slower                                                      |
| scimark_lu                 | 53.0 ms                                                     | 58.4 ms: 1.10x slower                                                      |
| logging_format             | 6.26 us                                                     | 6.91 us: 1.10x slower                                                      |
| sqlglot_normalize          | 175 ms                                                      | 193 ms: 1.11x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.1 ms: 1.11x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.11 sec: 1.11x slower                                                     |
| xml_etree_process          | 37.0 ms                                                     | 41.1 ms: 1.11x slower                                                      |
| pickle_pure_python         | 190 us                                                      | 210 us: 1.11x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 63.1 ms: 1.11x slower                                                      |
| chaos                      | 38.5 ms                                                     | 43.1 ms: 1.12x slower                                                      |
| float                      | 49.9 ms                                                     | 56.1 ms: 1.12x slower                                                      |
| hexiom                     | 3.89 ms                                                     | 4.37 ms: 1.12x slower                                                      |
| pyflate                    | 283 ms                                                      | 320 ms: 1.13x slower                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.58 sec: 1.13x slower                                                     |
| unpickle_pure_python       | 133 us                                                      | 151 us: 1.13x slower                                                       |
| scimark_fft                | 172 ms                                                      | 196 ms: 1.14x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 62.2 ns: 1.14x slower                                                      |
| regex_compile              | 80.5 ms                                                     | 91.8 ms: 1.14x slower                                                      |
| pycparser                  | 683 ms                                                      | 786 ms: 1.15x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 892 us: 1.16x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 1.11 ms: 1.16x slower                                                      |
| comprehensions             | 10.3 us                                                     | 11.9 us: 1.16x slower                                                      |
| fannkuch                   | 253 ms                                                      | 294 ms: 1.16x slower                                                       |
| django_template            | 22.4 ms                                                     | 26.0 ms: 1.16x slower                                                      |
| richards_super             | 30.9 ms                                                     | 35.9 ms: 1.16x slower                                                      |
| richards                   | 27.3 ms                                                     | 31.9 ms: 1.17x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 89.9 ms: 1.18x slower                                                      |
| deltablue                  | 1.92 ms                                                     | 2.28 ms: 1.19x slower                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 48.7 ms: 1.19x slower                                                      |
| raytrace                   | 160 ms                                                      | 195 ms: 1.22x slower                                                       |
| nbody                      | 68.4 ms                                                     | 83.7 ms: 1.22x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (5): json, regex_effbot, xml_etree_parse, genshi_xml, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-pythonperf1-amd64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.010x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown