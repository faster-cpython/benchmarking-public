# Results vs. 3.13.0

- fork: faster-cpython
- ref: fix_decref_and_reuse
- machine: windows-amd64
- commit hash: 07df2d0
- commit date: 2024-10-14
- overall geometric mean: 1.030x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 229 ms: 1.03x slower                                                                 |
| docutils       | 1.57 sec                                                    | 1.73 sec: 1.10x slower                                                               |
| html5lib       | 38.9 ms                                                     | 44.1 ms: 1.13x slower                                                                |
| tornado_http   | 93.0 ms                                                     | 94.2 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| coroutines       | 12.8 ms                                                     | 13.7 ms: 1.07x slower                                                                |
| async_generators | 223 ms                                                      | 247 ms: 1.11x slower                                                                 |
| Geometric mean   | (ref)                                                       | 1.09x slower                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                                 |
| float          | 49.9 ms                                                     | 53.3 ms: 1.07x slower                                                                |
| nbody          | 68.4 ms                                                     | 74.9 ms: 1.09x slower                                                                |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.6 ms: 1.38x faster                                                                |
| regex_effbot   | 1.58 ms                                                     | 1.64 ms: 1.04x slower                                                                |
| regex_dna      | 115 ms                                                      | 123 ms: 1.06x slower                                                                 |
| regex_compile  | 80.5 ms                                                     | 92.0 ms: 1.14x slower                                                                |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.6 ms                                                     | 97.0 ms: 1.04x slower                                                                |
| xml_etree_iterparse  | 61.8 ms                                                     | 65.5 ms: 1.06x slower                                                                |
| xml_etree_generate   | 54.0 ms                                                     | 57.4 ms: 1.06x slower                                                                |
| xml_etree_process    | 37.0 ms                                                     | 40.8 ms: 1.10x slower                                                                |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.12x slower                                                                 |
| pickle_pure_python   | 190 us                                                      | 216 us: 1.14x slower                                                                 |
| json_dumps           | 5.92 ms                                                     | 6.78 ms: 1.15x slower                                                                |
| tomli_loads          | 1.39 sec                                                    | 1.62 sec: 1.16x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                         |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.2 ms: 1.14x faster                                                                |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 38.1 ms: 1.07x slower                                                                |
| genshi_text     | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                                |
| mako            | 6.35 ms                                                     | 7.01 ms: 1.10x slower                                                                |
| django_template | 22.4 ms                                                     | 25.7 ms: 1.15x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                   | 8.80 ms                                                     | 521 us: 16.89x faster                                                                |
| regex_v8                 | 21.4 ms                                                     | 15.6 ms: 1.38x faster                                                                |
| create_gc_cycles         | 1.26 ms                                                     | 940 us: 1.34x faster                                                                 |
| gc_traversal             | 1.97 ms                                                     | 1.55 ms: 1.27x faster                                                                |
| bench_mp_pool            | 86.4 ms                                                     | 69.6 ms: 1.24x faster                                                                |
| deepcopy                 | 226 us                                                      | 189 us: 1.20x faster                                                                 |
| deepcopy_memo            | 23.3 us                                                     | 20.0 us: 1.16x faster                                                                |
| python_startup           | 25.4 ms                                                     | 22.2 ms: 1.14x faster                                                                |
| deepcopy_reduce          | 2.06 us                                                     | 1.95 us: 1.06x faster                                                                |
| bench_thread_pool        | 847 us                                                      | 809 us: 1.05x faster                                                                 |
| go                       | 87.0 ms                                                     | 87.9 ms: 1.01x slower                                                                |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                                                 |
| tornado_http             | 93.0 ms                                                     | 94.2 ms: 1.01x slower                                                                |
| sympy_sum                | 86.9 ms                                                     | 89.3 ms: 1.03x slower                                                                |
| 2to3                     | 221 ms                                                      | 229 ms: 1.03x slower                                                                 |
| xml_etree_parse          | 93.6 ms                                                     | 97.0 ms: 1.04x slower                                                                |
| meteor_contest           | 73.5 ms                                                     | 76.5 ms: 1.04x slower                                                                |
| regex_effbot             | 1.58 ms                                                     | 1.64 ms: 1.04x slower                                                                |
| coverage                 | 45.6 ms                                                     | 47.5 ms: 1.04x slower                                                                |
| sympy_expand             | 291 ms                                                      | 306 ms: 1.05x slower                                                                 |
| mdp                      | 1.39 sec                                                    | 1.46 sec: 1.05x slower                                                               |
| sympy_str                | 169 ms                                                      | 178 ms: 1.05x slower                                                                 |
| xml_etree_iterparse      | 61.8 ms                                                     | 65.5 ms: 1.06x slower                                                                |
| typing_runtime_protocols | 105 us                                                      | 112 us: 1.06x slower                                                                 |
| xml_etree_generate       | 54.0 ms                                                     | 57.4 ms: 1.06x slower                                                                |
| regex_dna                | 115 ms                                                      | 123 ms: 1.06x slower                                                                 |
| crypto_pyaes             | 45.4 ms                                                     | 48.4 ms: 1.06x slower                                                                |
| float                    | 49.9 ms                                                     | 53.3 ms: 1.07x slower                                                                |
| sympy_integrate          | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                                |
| genshi_xml               | 35.5 ms                                                     | 38.1 ms: 1.07x slower                                                                |
| coroutines               | 12.8 ms                                                     | 13.7 ms: 1.07x slower                                                                |
| pylint                   | 211 ms                                                      | 228 ms: 1.08x slower                                                                 |
| logging_simple           | 5.96 us                                                     | 6.44 us: 1.08x slower                                                                |
| dulwich_log              | 40.8 ms                                                     | 44.2 ms: 1.08x slower                                                                |
| pycparser                | 683 ms                                                      | 739 ms: 1.08x slower                                                                 |
| logging_format           | 6.26 us                                                     | 6.79 us: 1.09x slower                                                                |
| spectral_norm            | 62.8 ms                                                     | 68.2 ms: 1.09x slower                                                                |
| pprint_safe_repr         | 494 ms                                                      | 540 ms: 1.09x slower                                                                 |
| nbody                    | 68.4 ms                                                     | 74.9 ms: 1.09x slower                                                                |
| docutils                 | 1.57 sec                                                    | 1.73 sec: 1.10x slower                                                               |
| genshi_text              | 15.6 ms                                                     | 17.1 ms: 1.10x slower                                                                |
| xml_etree_process        | 37.0 ms                                                     | 40.8 ms: 1.10x slower                                                                |
| fannkuch                 | 253 ms                                                      | 279 ms: 1.10x slower                                                                 |
| mako                     | 6.35 ms                                                     | 7.01 ms: 1.10x slower                                                                |
| async_generators         | 223 ms                                                      | 247 ms: 1.11x slower                                                                 |
| nqueens                  | 56.7 ms                                                     | 62.8 ms: 1.11x slower                                                                |
| sqlglot_optimize         | 32.9 ms                                                     | 36.6 ms: 1.11x slower                                                                |
| sqlglot_normalize        | 175 ms                                                      | 194 ms: 1.11x slower                                                                 |
| scimark_sparse_mat_mult  | 2.46 ms                                                     | 2.73 ms: 1.11x slower                                                                |
| chaos                    | 38.5 ms                                                     | 43.1 ms: 1.12x slower                                                                |
| pprint_pformat           | 999 ms                                                      | 1.12 sec: 1.12x slower                                                               |
| unpickle_pure_python     | 133 us                                                      | 149 us: 1.12x slower                                                                 |
| logging_silent           | 54.6 ns                                                     | 61.7 ns: 1.13x slower                                                                |
| html5lib                 | 38.9 ms                                                     | 44.1 ms: 1.13x slower                                                                |
| generators               | 19.5 ms                                                     | 22.1 ms: 1.13x slower                                                                |
| hexiom                   | 3.89 ms                                                     | 4.43 ms: 1.14x slower                                                                |
| pickle_pure_python       | 190 us                                                      | 216 us: 1.14x slower                                                                 |
| pyflate                  | 283 ms                                                      | 323 ms: 1.14x slower                                                                 |
| regex_compile            | 80.5 ms                                                     | 92.0 ms: 1.14x slower                                                                |
| comprehensions           | 10.3 us                                                     | 11.7 us: 1.14x slower                                                                |
| scimark_fft              | 172 ms                                                      | 197 ms: 1.15x slower                                                                 |
| json_dumps               | 5.92 ms                                                     | 6.78 ms: 1.15x slower                                                                |
| django_template          | 22.4 ms                                                     | 25.7 ms: 1.15x slower                                                                |
| tomli_loads              | 1.39 sec                                                    | 1.62 sec: 1.16x slower                                                               |
| scimark_monte_carlo      | 40.8 ms                                                     | 47.5 ms: 1.16x slower                                                                |
| scimark_sor              | 76.2 ms                                                     | 89.7 ms: 1.18x slower                                                                |
| sqlglot_transpile        | 956 us                                                      | 1.13 ms: 1.19x slower                                                                |
| scimark_lu               | 53.0 ms                                                     | 62.9 ms: 1.19x slower                                                                |
| raytrace                 | 160 ms                                                      | 191 ms: 1.19x slower                                                                 |
| sqlglot_parse            | 771 us                                                      | 920 us: 1.19x slower                                                                 |
| richards                 | 27.3 ms                                                     | 32.7 ms: 1.20x slower                                                                |
| richards_super           | 30.9 ms                                                     | 37.3 ms: 1.21x slower                                                                |
| deltablue                | 1.92 ms                                                     | 2.34 ms: 1.22x slower                                                                |
| json                     | 3.19 ms                                                     | 4.52 ms: 1.42x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.03x slower                                                                         |

Benchmark hidden because not significant (4): json_loads, pathlib, python_startup_no_site, telco
Ignored benchmarks (19) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241014-3.14.0a0-07df2d0/bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown