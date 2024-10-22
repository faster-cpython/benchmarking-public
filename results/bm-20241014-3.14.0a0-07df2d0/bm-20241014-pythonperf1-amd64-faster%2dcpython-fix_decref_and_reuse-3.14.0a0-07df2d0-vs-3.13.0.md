# Results vs. 3.13.0

- fork: faster-cpython
- ref: fix_decref_and_reuse
- machine: windows-amd64
- commit hash: 07df2d0
- commit date: 2024-10-14
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 229 ms: 1.05x slower                                                                 |
| docutils       | 1.57 sec                                                    | 1.73 sec: 1.10x slower                                                               |
| html5lib       | 38.6 ms                                                     | 44.1 ms: 1.14x slower                                                                |
| tornado_http   | 92.8 ms                                                     | 94.2 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| coroutines       | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                                |
| async_generators | 223 ms                                                      | 247 ms: 1.11x slower                                                                 |
| Geometric mean   | (ref)                                                       | 1.06x slower                                                                         |

Benchmark hidden because not significant (2): asyncio_tcp, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                                 |
| float          | 48.1 ms                                                     | 53.3 ms: 1.11x slower                                                                |
| nbody          | 64.5 ms                                                     | 74.9 ms: 1.16x slower                                                                |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.64 ms: 1.02x slower                                                                |
| regex_v8       | 14.7 ms                                                     | 15.6 ms: 1.06x slower                                                                |
| regex_dna      | 114 ms                                                      | 123 ms: 1.07x slower                                                                 |
| regex_compile  | 80.1 ms                                                     | 92.0 ms: 1.15x slower                                                                |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 7.19 us: 1.02x faster                                                                |
| xml_etree_parse      | 93.2 ms                                                     | 97.0 ms: 1.04x slower                                                                |
| json_loads           | 14.3 us                                                     | 15.0 us: 1.05x slower                                                                |
| unpickle_list        | 2.72 us                                                     | 2.85 us: 1.05x slower                                                                |
| xml_etree_iterparse  | 62.3 ms                                                     | 65.5 ms: 1.05x slower                                                                |
| pickle_dict          | 18.0 us                                                     | 19.1 us: 1.06x slower                                                                |
| xml_etree_generate   | 53.3 ms                                                     | 57.4 ms: 1.08x slower                                                                |
| unpickle             | 8.63 us                                                     | 9.30 us: 1.08x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 40.8 ms: 1.12x slower                                                                |
| json_dumps           | 5.76 ms                                                     | 6.78 ms: 1.18x slower                                                                |
| pickle_pure_python   | 183 us                                                      | 216 us: 1.18x slower                                                                 |
| unpickle_pure_python | 127 us                                                      | 149 us: 1.18x slower                                                                 |
| tomli_loads          | 1.36 sec                                                    | 1.62 sec: 1.19x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                         |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                         |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 7.01 ms: 1.12x slower                                                                |
| genshi_text     | 14.9 ms                                                     | 17.1 ms: 1.15x slower                                                                |
| genshi_xml      | 32.8 ms                                                     | 38.1 ms: 1.16x slower                                                                |
| django_template | 21.8 ms                                                     | 25.7 ms: 1.18x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                   | 8.68 ms                                                     | 521 us: 16.67x faster                                                                |
| deepcopy                 | 223 us                                                      | 189 us: 1.18x faster                                                                 |
| deepcopy_memo            | 21.8 us                                                     | 20.0 us: 1.09x faster                                                                |
| unpack_sequence          | 40.0 ns                                                     | 38.4 ns: 1.04x faster                                                                |
| deepcopy_reduce          | 2.02 us                                                     | 1.95 us: 1.04x faster                                                                |
| bench_thread_pool        | 828 us                                                      | 809 us: 1.02x faster                                                                 |
| pickle                   | 7.34 us                                                     | 7.19 us: 1.02x faster                                                                |
| telco                    | 4.85 ms                                                     | 4.79 ms: 1.01x faster                                                                |
| pathlib                  | 81.2 ms                                                     | 80.6 ms: 1.01x faster                                                                |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                                                 |
| tornado_http             | 92.8 ms                                                     | 94.2 ms: 1.01x slower                                                                |
| regex_effbot             | 1.62 ms                                                     | 1.64 ms: 1.02x slower                                                                |
| python_startup_no_site   | 17.8 ms                                                     | 18.1 ms: 1.02x slower                                                                |
| coverage                 | 46.7 ms                                                     | 47.5 ms: 1.02x slower                                                                |
| sqlite_synth             | 1.60 us                                                     | 1.64 us: 1.03x slower                                                                |
| sympy_sum                | 86.4 ms                                                     | 89.3 ms: 1.03x slower                                                                |
| go                       | 84.6 ms                                                     | 87.9 ms: 1.04x slower                                                                |
| xml_etree_parse          | 93.2 ms                                                     | 97.0 ms: 1.04x slower                                                                |
| json_loads               | 14.3 us                                                     | 15.0 us: 1.05x slower                                                                |
| unpickle_list            | 2.72 us                                                     | 2.85 us: 1.05x slower                                                                |
| xml_etree_iterparse      | 62.3 ms                                                     | 65.5 ms: 1.05x slower                                                                |
| 2to3                     | 217 ms                                                      | 229 ms: 1.05x slower                                                                 |
| mdp                      | 1.38 sec                                                    | 1.46 sec: 1.05x slower                                                               |
| pickle_dict              | 18.0 us                                                     | 19.1 us: 1.06x slower                                                                |
| meteor_contest           | 72.3 ms                                                     | 76.5 ms: 1.06x slower                                                                |
| regex_v8                 | 14.7 ms                                                     | 15.6 ms: 1.06x slower                                                                |
| sympy_str                | 166 ms                                                      | 178 ms: 1.07x slower                                                                 |
| regex_dna                | 114 ms                                                      | 123 ms: 1.07x slower                                                                 |
| sympy_expand             | 285 ms                                                      | 306 ms: 1.07x slower                                                                 |
| xml_etree_generate       | 53.3 ms                                                     | 57.4 ms: 1.08x slower                                                                |
| unpickle                 | 8.63 us                                                     | 9.30 us: 1.08x slower                                                                |
| pylint                   | 211 ms                                                      | 228 ms: 1.08x slower                                                                 |
| sympy_integrate          | 12.3 ms                                                     | 13.4 ms: 1.09x slower                                                                |
| coroutines               | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                                |
| dulwich_log              | 40.4 ms                                                     | 44.2 ms: 1.09x slower                                                                |
| pprint_safe_repr         | 493 ms                                                      | 540 ms: 1.10x slower                                                                 |
| docutils                 | 1.57 sec                                                    | 1.73 sec: 1.10x slower                                                               |
| logging_format           | 6.15 us                                                     | 6.79 us: 1.10x slower                                                                |
| sqlglot_optimize         | 33.1 ms                                                     | 36.6 ms: 1.11x slower                                                                |
| float                    | 48.1 ms                                                     | 53.3 ms: 1.11x slower                                                                |
| async_generators         | 223 ms                                                      | 247 ms: 1.11x slower                                                                 |
| typing_runtime_protocols | 100 us                                                      | 112 us: 1.11x slower                                                                 |
| xml_etree_process        | 36.5 ms                                                     | 40.8 ms: 1.12x slower                                                                |
| mako                     | 6.24 ms                                                     | 7.01 ms: 1.12x slower                                                                |
| logging_simple           | 5.72 us                                                     | 6.44 us: 1.12x slower                                                                |
| pprint_pformat           | 991 ms                                                      | 1.12 sec: 1.13x slower                                                               |
| crypto_pyaes             | 42.8 ms                                                     | 48.4 ms: 1.13x slower                                                                |
| nqueens                  | 55.5 ms                                                     | 62.8 ms: 1.13x slower                                                                |
| scimark_fft              | 174 ms                                                      | 197 ms: 1.13x slower                                                                 |
| create_gc_cycles         | 829 us                                                      | 940 us: 1.13x slower                                                                 |
| generators               | 19.5 ms                                                     | 22.1 ms: 1.13x slower                                                                |
| sqlglot_normalize        | 171 ms                                                      | 194 ms: 1.14x slower                                                                 |
| chaos                    | 37.9 ms                                                     | 43.1 ms: 1.14x slower                                                                |
| fannkuch                 | 245 ms                                                      | 279 ms: 1.14x slower                                                                 |
| html5lib                 | 38.6 ms                                                     | 44.1 ms: 1.14x slower                                                                |
| comprehensions           | 10.2 us                                                     | 11.7 us: 1.15x slower                                                                |
| regex_compile            | 80.1 ms                                                     | 92.0 ms: 1.15x slower                                                                |
| spectral_norm            | 59.2 ms                                                     | 68.2 ms: 1.15x slower                                                                |
| genshi_text              | 14.9 ms                                                     | 17.1 ms: 1.15x slower                                                                |
| nbody                    | 64.5 ms                                                     | 74.9 ms: 1.16x slower                                                                |
| genshi_xml               | 32.8 ms                                                     | 38.1 ms: 1.16x slower                                                                |
| scimark_lu               | 54.0 ms                                                     | 62.9 ms: 1.17x slower                                                                |
| scimark_sparse_mat_mult  | 2.34 ms                                                     | 2.73 ms: 1.17x slower                                                                |
| pyflate                  | 275 ms                                                      | 323 ms: 1.17x slower                                                                 |
| json_dumps               | 5.76 ms                                                     | 6.78 ms: 1.18x slower                                                                |
| pickle_pure_python       | 183 us                                                      | 216 us: 1.18x slower                                                                 |
| unpickle_pure_python     | 127 us                                                      | 149 us: 1.18x slower                                                                 |
| django_template          | 21.8 ms                                                     | 25.7 ms: 1.18x slower                                                                |
| scimark_monte_carlo      | 40.3 ms                                                     | 47.5 ms: 1.18x slower                                                                |
| tomli_loads              | 1.36 sec                                                    | 1.62 sec: 1.19x slower                                                               |
| sqlglot_transpile        | 952 us                                                      | 1.13 ms: 1.19x slower                                                                |
| hexiom                   | 3.69 ms                                                     | 4.43 ms: 1.20x slower                                                                |
| sqlglot_parse            | 761 us                                                      | 920 us: 1.21x slower                                                                 |
| logging_silent           | 51.0 ns                                                     | 61.7 ns: 1.21x slower                                                                |
| raytrace                 | 156 ms                                                      | 191 ms: 1.22x slower                                                                 |
| scimark_sor              | 72.0 ms                                                     | 89.7 ms: 1.25x slower                                                                |
| deltablue                | 1.86 ms                                                     | 2.34 ms: 1.25x slower                                                                |
| richards                 | 26.0 ms                                                     | 32.7 ms: 1.26x slower                                                                |
| richards_super           | 29.3 ms                                                     | 37.3 ms: 1.27x slower                                                                |
| json                     | 2.98 ms                                                     | 4.52 ms: 1.52x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.06x slower                                                                         |

Benchmark hidden because not significant (7): pycparser, asyncio_tcp, gc_traversal, bench_mp_pool, python_startup, pickle_list, asyncio_tcp_ssl
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, flaskblogging, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown