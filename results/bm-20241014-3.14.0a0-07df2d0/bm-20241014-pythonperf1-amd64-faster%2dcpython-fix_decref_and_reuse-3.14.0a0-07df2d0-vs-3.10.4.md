# Results vs. 3.10.4

- fork: faster-cpython
- ref: fix_decref_and_reuse
- machine: windows-amd64
- commit hash: 07df2d0
- commit date: 2024-10-14
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 229 ms: 1.07x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                               |
| html5lib       | 51.0 ms                                                     | 44.1 ms: 1.16x faster                                                                |
| tornado_http   | 108 ms                                                      | 94.2 ms: 1.15x faster                                                                |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 53.3 ms: 1.16x faster                                                                |
| nbody          | 71.3 ms                                                     | 74.9 ms: 1.05x slower                                                                |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 92.0 ms: 1.15x faster                                                                |
| regex_dna      | 136 ms                                                      | 123 ms: 1.11x faster                                                                 |
| regex_effbot   | 1.66 ms                                                     | 1.64 ms: 1.01x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 15.6 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.78 ms: 1.35x faster                                                                |
| pickle_pure_python   | 270 us                                                      | 216 us: 1.25x faster                                                                 |
| unpickle_pure_python | 183 us                                                      | 149 us: 1.23x faster                                                                 |
| xml_etree_process    | 44.5 ms                                                     | 40.8 ms: 1.09x faster                                                                |
| tomli_loads          | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                               |
| unpickle             | 9.09 us                                                     | 9.30 us: 1.02x slower                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 57.4 ms: 1.03x slower                                                                |
| pickle               | 6.85 us                                                     | 7.19 us: 1.05x slower                                                                |
| unpickle_list        | 2.71 us                                                     | 2.85 us: 1.05x slower                                                                |
| pickle_list          | 2.75 us                                                     | 2.92 us: 1.06x slower                                                                |
| json_loads           | 14.0 us                                                     | 15.0 us: 1.07x slower                                                                |
| pickle_dict          | 17.2 us                                                     | 19.1 us: 1.11x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                         |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                                |
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.01 ms: 1.29x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                                |
| django_template | 28.9 ms                                                     | 25.7 ms: 1.12x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 38.1 ms: 1.08x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.00x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.34 ms: 1.79x faster                                                                |
| go                       | 139 ms                                                      | 87.9 ms: 1.58x faster                                                                |
| pylint                   | 350 ms                                                      | 228 ms: 1.54x faster                                                                 |
| logging_silent           | 94.6 ns                                                     | 61.7 ns: 1.53x faster                                                                |
| generators               | 32.4 ms                                                     | 22.1 ms: 1.47x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 20.0 us: 1.44x faster                                                                |
| raytrace                 | 273 ms                                                      | 191 ms: 1.43x faster                                                                 |
| chaos                    | 61.7 ms                                                     | 43.1 ms: 1.43x faster                                                                |
| comprehensions           | 16.5 us                                                     | 11.7 us: 1.41x faster                                                                |
| richards_super           | 52.2 ms                                                     | 37.3 ms: 1.40x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 62.9 ms: 1.36x faster                                                                |
| deepcopy                 | 255 us                                                      | 189 us: 1.35x faster                                                                 |
| json_dumps               | 9.16 ms                                                     | 6.78 ms: 1.35x faster                                                                |
| sqlglot_parse            | 1.22 ms                                                     | 920 us: 1.32x faster                                                                 |
| sqlglot_transpile        | 1.48 ms                                                     | 1.13 ms: 1.30x faster                                                                |
| richards                 | 42.4 ms                                                     | 32.7 ms: 1.30x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.43 ms: 1.30x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 48.4 ms: 1.29x faster                                                                |
| mako                     | 9.03 ms                                                     | 7.01 ms: 1.29x faster                                                                |
| pyflate                  | 409 ms                                                      | 323 ms: 1.27x faster                                                                 |
| pycparser                | 930 ms                                                      | 739 ms: 1.26x faster                                                                 |
| pickle_pure_python       | 270 us                                                      | 216 us: 1.25x faster                                                                 |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.71 sec: 1.23x faster                                                               |
| unpickle_pure_python     | 183 us                                                      | 149 us: 1.23x faster                                                                 |
| mdp                      | 1.78 sec                                                    | 1.46 sec: 1.22x faster                                                               |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.5 ms: 1.21x faster                                                                |
| sympy_sum                | 107 ms                                                      | 89.3 ms: 1.20x faster                                                                |
| thrift                   | 617 us                                                      | 521 us: 1.19x faster                                                                 |
| bench_thread_pool        | 958 us                                                      | 809 us: 1.18x faster                                                                 |
| scimark_sor              | 106 ms                                                      | 89.7 ms: 1.18x faster                                                                |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                                |
| sqlite_synth             | 1.91 us                                                     | 1.64 us: 1.17x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 44.1 ms: 1.16x faster                                                                |
| float                    | 61.7 ms                                                     | 53.3 ms: 1.16x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                                |
| regex_compile            | 106 ms                                                      | 92.0 ms: 1.15x faster                                                                |
| tornado_http             | 108 ms                                                      | 94.2 ms: 1.15x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 44.2 ms: 1.14x faster                                                                |
| asyncio_tcp              | 732 ms                                                      | 646 ms: 1.13x faster                                                                 |
| spectral_norm            | 77.3 ms                                                     | 68.2 ms: 1.13x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                                                |
| django_template          | 28.9 ms                                                     | 25.7 ms: 1.12x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                               |
| regex_dna                | 136 ms                                                      | 123 ms: 1.11x faster                                                                 |
| pprint_safe_repr         | 592 ms                                                      | 540 ms: 1.10x faster                                                                 |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                                 |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                               |
| xml_etree_process        | 44.5 ms                                                     | 40.8 ms: 1.09x faster                                                                |
| sqlglot_optimize         | 39.8 ms                                                     | 36.6 ms: 1.09x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 38.1 ms: 1.08x faster                                                                |
| 2to3                     | 246 ms                                                      | 229 ms: 1.07x faster                                                                 |
| nqueens                  | 66.6 ms                                                     | 62.8 ms: 1.06x faster                                                                |
| sqlglot_normalize        | 205 ms                                                      | 194 ms: 1.06x faster                                                                 |
| unpack_sequence          | 39.6 ns                                                     | 38.4 ns: 1.03x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                               |
| sympy_expand             | 314 ms                                                      | 306 ms: 1.03x faster                                                                 |
| regex_effbot             | 1.66 ms                                                     | 1.64 ms: 1.01x faster                                                                |
| meteor_contest           | 75.9 ms                                                     | 76.5 ms: 1.01x slower                                                                |
| regex_v8                 | 15.4 ms                                                     | 15.6 ms: 1.01x slower                                                                |
| unpickle                 | 9.09 us                                                     | 9.30 us: 1.02x slower                                                                |
| xml_etree_generate       | 55.5 ms                                                     | 57.4 ms: 1.03x slower                                                                |
| logging_simple           | 6.22 us                                                     | 6.44 us: 1.03x slower                                                                |
| pickle                   | 6.85 us                                                     | 7.19 us: 1.05x slower                                                                |
| nbody                    | 71.3 ms                                                     | 74.9 ms: 1.05x slower                                                                |
| unpickle_list            | 2.71 us                                                     | 2.85 us: 1.05x slower                                                                |
| scimark_fft              | 187 ms                                                      | 197 ms: 1.05x slower                                                                 |
| pickle_list              | 2.75 us                                                     | 2.92 us: 1.06x slower                                                                |
| pathlib                  | 75.7 ms                                                     | 80.6 ms: 1.06x slower                                                                |
| json_loads               | 14.0 us                                                     | 15.0 us: 1.07x slower                                                                |
| python_startup           | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                                |
| fannkuch                 | 256 ms                                                      | 279 ms: 1.09x slower                                                                 |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                                |
| pickle_dict              | 17.2 us                                                     | 19.1 us: 1.11x slower                                                                |
| async_generators         | 222 ms                                                      | 247 ms: 1.11x slower                                                                 |
| bench_mp_pool            | 62.0 ms                                                     | 69.6 ms: 1.12x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 940 us: 1.18x slower                                                                 |
| telco                    | 3.94 ms                                                     | 4.79 ms: 1.22x slower                                                                |
| coverage                 | 39.0 ms                                                     | 47.5 ms: 1.22x slower                                                                |
| json                     | 3.14 ms                                                     | 4.52 ms: 1.44x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.13x faster                                                                         |

Benchmark hidden because not significant (5): xml_etree_parse, pidigits, scimark_sparse_mat_mult, logging_format, xml_etree_iterparse
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown