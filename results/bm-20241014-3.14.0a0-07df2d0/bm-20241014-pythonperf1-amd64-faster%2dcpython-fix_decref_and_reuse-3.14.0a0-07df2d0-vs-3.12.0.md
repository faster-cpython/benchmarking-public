# Results vs. 3.12.0

- fork: faster-cpython
- ref: fix_decref_and_reuse
- machine: windows-amd64
- commit hash: 07df2d0
- commit date: 2024-10-14
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 229 ms: 1.05x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                               |
| tornado_http   | 89.5 ms                                                     | 94.2 ms: 1.05x slower                                                                |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 53.3 ms: 1.07x faster                                                                |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                                 |
| nbody          | 71.9 ms                                                     | 74.9 ms: 1.04x slower                                                                |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 123 ms: 1.03x faster                                                                 |
| regex_effbot   | 1.62 ms                                                     | 1.64 ms: 1.01x slower                                                                |
| regex_compile  | 87.5 ms                                                     | 92.0 ms: 1.05x slower                                                                |
| regex_v8       | 14.2 ms                                                     | 15.6 ms: 1.09x slower                                                                |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.19 us: 1.03x faster                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 57.4 ms: 1.03x slower                                                                |
| pickle_list          | 2.83 us                                                     | 2.92 us: 1.03x slower                                                                |
| pickle_dict          | 18.4 us                                                     | 19.1 us: 1.04x slower                                                                |
| unpickle_list        | 2.75 us                                                     | 2.85 us: 1.04x slower                                                                |
| xml_etree_parse      | 93.0 ms                                                     | 97.0 ms: 1.04x slower                                                                |
| json_loads           | 13.9 us                                                     | 15.0 us: 1.08x slower                                                                |
| xml_etree_process    | 37.7 ms                                                     | 40.8 ms: 1.08x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 216 us: 1.11x slower                                                                 |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.12x slower                                                                 |
| unpickle             | 8.18 us                                                     | 9.30 us: 1.14x slower                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.62 sec: 1.19x slower                                                               |
| json_dumps           | 5.70 ms                                                     | 6.78 ms: 1.19x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                                |
| python_startup         | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.01 ms: 1.01x faster                                                                |
| django_template | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| deepcopy                 | 238 us                                                      | 189 us: 1.26x faster                                                                 |
| asyncio_tcp_ssl          | 2.10 sec                                                    | 1.71 sec: 1.22x faster                                                               |
| comprehensions           | 14.1 us                                                     | 11.7 us: 1.20x faster                                                                |
| deepcopy_memo            | 23.7 us                                                     | 20.0 us: 1.18x faster                                                                |
| deepcopy_reduce          | 2.09 us                                                     | 1.95 us: 1.08x faster                                                                |
| sqlite_synth             | 1.76 us                                                     | 1.64 us: 1.07x faster                                                                |
| float                    | 56.8 ms                                                     | 53.3 ms: 1.07x faster                                                                |
| bench_thread_pool        | 857 us                                                      | 809 us: 1.06x faster                                                                 |
| go                       | 91.6 ms                                                     | 87.9 ms: 1.04x faster                                                                |
| coroutines               | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                                |
| pickle                   | 7.43 us                                                     | 7.19 us: 1.03x faster                                                                |
| regex_dna                | 126 ms                                                      | 123 ms: 1.03x faster                                                                 |
| sympy_sum                | 91.5 ms                                                     | 89.3 ms: 1.03x faster                                                                |
| generators               | 22.5 ms                                                     | 22.1 ms: 1.02x faster                                                                |
| pidigits                 | 152 ms                                                      | 150 ms: 1.02x faster                                                                 |
| mako                     | 7.09 ms                                                     | 7.01 ms: 1.01x faster                                                                |
| raytrace                 | 192 ms                                                      | 191 ms: 1.01x faster                                                                 |
| chaos                    | 43.3 ms                                                     | 43.1 ms: 1.01x faster                                                                |
| bench_mp_pool            | 69.2 ms                                                     | 69.6 ms: 1.01x slower                                                                |
| logging_format           | 6.72 us                                                     | 6.79 us: 1.01x slower                                                                |
| regex_effbot             | 1.62 ms                                                     | 1.64 ms: 1.01x slower                                                                |
| sympy_str                | 175 ms                                                      | 178 ms: 1.01x slower                                                                 |
| gc_traversal             | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                                |
| spectral_norm            | 66.9 ms                                                     | 68.2 ms: 1.02x slower                                                                |
| logging_silent           | 60.5 ns                                                     | 61.7 ns: 1.02x slower                                                                |
| unpack_sequence          | 37.5 ns                                                     | 38.4 ns: 1.02x slower                                                                |
| meteor_contest           | 74.6 ms                                                     | 76.5 ms: 1.02x slower                                                                |
| logging_simple           | 6.28 us                                                     | 6.44 us: 1.03x slower                                                                |
| xml_etree_generate       | 55.8 ms                                                     | 57.4 ms: 1.03x slower                                                                |
| sympy_integrate          | 13.0 ms                                                     | 13.4 ms: 1.03x slower                                                                |
| async_generators         | 239 ms                                                      | 247 ms: 1.03x slower                                                                 |
| pickle_list              | 2.83 us                                                     | 2.92 us: 1.03x slower                                                                |
| pickle_dict              | 18.4 us                                                     | 19.1 us: 1.04x slower                                                                |
| unpickle_list            | 2.75 us                                                     | 2.85 us: 1.04x slower                                                                |
| docutils                 | 1.66 sec                                                    | 1.73 sec: 1.04x slower                                                               |
| sqlglot_normalize        | 187 ms                                                      | 194 ms: 1.04x slower                                                                 |
| nbody                    | 71.9 ms                                                     | 74.9 ms: 1.04x slower                                                                |
| xml_etree_parse          | 93.0 ms                                                     | 97.0 ms: 1.04x slower                                                                |
| 2to3                     | 218 ms                                                      | 229 ms: 1.05x slower                                                                 |
| regex_compile            | 87.5 ms                                                     | 92.0 ms: 1.05x slower                                                                |
| pprint_safe_repr         | 513 ms                                                      | 540 ms: 1.05x slower                                                                 |
| tornado_http             | 89.5 ms                                                     | 94.2 ms: 1.05x slower                                                                |
| pycparser                | 699 ms                                                      | 739 ms: 1.06x slower                                                                 |
| sqlglot_optimize         | 34.5 ms                                                     | 36.6 ms: 1.06x slower                                                                |
| mdp                      | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                               |
| scimark_sparse_mat_mult  | 2.56 ms                                                     | 2.73 ms: 1.07x slower                                                                |
| scimark_lu               | 58.9 ms                                                     | 62.9 ms: 1.07x slower                                                                |
| scimark_fft              | 184 ms                                                      | 197 ms: 1.07x slower                                                                 |
| pprint_pformat           | 1.05 sec                                                    | 1.12 sec: 1.07x slower                                                               |
| json_loads               | 13.9 us                                                     | 15.0 us: 1.08x slower                                                                |
| sympy_expand             | 284 ms                                                      | 306 ms: 1.08x slower                                                                 |
| hexiom                   | 4.10 ms                                                     | 4.43 ms: 1.08x slower                                                                |
| xml_etree_process        | 37.7 ms                                                     | 40.8 ms: 1.08x slower                                                                |
| deltablue                | 2.16 ms                                                     | 2.34 ms: 1.08x slower                                                                |
| scimark_monte_carlo      | 43.7 ms                                                     | 47.5 ms: 1.09x slower                                                                |
| regex_v8                 | 14.2 ms                                                     | 15.6 ms: 1.09x slower                                                                |
| pyflate                  | 295 ms                                                      | 323 ms: 1.10x slower                                                                 |
| pickle_pure_python       | 195 us                                                      | 216 us: 1.11x slower                                                                 |
| sqlglot_transpile        | 1.02 ms                                                     | 1.13 ms: 1.11x slower                                                                |
| python_startup_no_site   | 16.2 ms                                                     | 18.1 ms: 1.11x slower                                                                |
| django_template          | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                                |
| unpickle_pure_python     | 133 us                                                      | 149 us: 1.12x slower                                                                 |
| fannkuch                 | 247 ms                                                      | 279 ms: 1.13x slower                                                                 |
| unpickle                 | 8.18 us                                                     | 9.30 us: 1.14x slower                                                                |
| scimark_sor              | 78.8 ms                                                     | 89.7 ms: 1.14x slower                                                                |
| python_startup           | 19.5 ms                                                     | 22.2 ms: 1.14x slower                                                                |
| sqlglot_parse            | 804 us                                                      | 920 us: 1.14x slower                                                                 |
| richards                 | 28.4 ms                                                     | 32.7 ms: 1.15x slower                                                                |
| telco                    | 4.13 ms                                                     | 4.79 ms: 1.16x slower                                                                |
| richards_super           | 32.1 ms                                                     | 37.3 ms: 1.16x slower                                                                |
| coverage                 | 40.8 ms                                                     | 47.5 ms: 1.16x slower                                                                |
| typing_runtime_protocols | 95.1 us                                                     | 112 us: 1.18x slower                                                                 |
| tomli_loads              | 1.37 sec                                                    | 1.62 sec: 1.19x slower                                                               |
| json_dumps               | 5.70 ms                                                     | 6.78 ms: 1.19x slower                                                                |
| create_gc_cycles         | 752 us                                                      | 940 us: 1.25x slower                                                                 |
| asyncio_tcp              | 487 ms                                                      | 646 ms: 1.33x slower                                                                 |
| json                     | 3.05 ms                                                     | 4.52 ms: 1.48x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.05x slower                                                                         |

Benchmark hidden because not significant (5): dulwich_log, crypto_pyaes, nqueens, pathlib, xml_etree_iterparse
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241014-3.14.0a0-07df2d0/bm-20241014-pythonperf1-amd64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown