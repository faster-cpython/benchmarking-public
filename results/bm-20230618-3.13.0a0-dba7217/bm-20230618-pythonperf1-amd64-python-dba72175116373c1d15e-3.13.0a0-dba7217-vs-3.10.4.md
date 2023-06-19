
# Results vs. 3.10.4

- fork: python
- ref: dba72175116373c1d15e
- machine: windows-amd64
- commit hash: dba7217
- commit date: 2023-06-18
- overall geometric mean: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf1-amd64-python-dba72175116373c1d15e-3.13.0a0-dba7217 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.64 sec: 1.15x faster                                                     |
| tornado_http   | 109 ms                                                      | 90.5 ms: 1.20x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf1-amd64-python-dba72175116373c1d15e-3.13.0a0-dba7217 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 56.3 ms: 1.07x faster                                                      |
| pidigits       | 145 ms                                                      | 150 ms: 1.04x slower                                                       |
| nbody          | 69.3 ms                                                     | 74.9 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf1-amd64-python-dba72175116373c1d15e-3.13.0a0-dba7217 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 88.2 ms: 1.17x faster                                                      |
| regex_dna      | 132 ms                                                      | 124 ms: 1.06x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf1-amd64-python-dba72175116373c1d15e-3.13.0a0-dba7217 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.76 ms: 1.48x faster                                                      |
| pickle_pure_python   | 257 us                                                      | 193 us: 1.33x faster                                                       |
| unpickle_pure_python | 171 us                                                      | 133 us: 1.28x faster                                                       |
| tomli_loads          | 1.62 sec                                                    | 1.43 sec: 1.13x faster                                                     |
| unpickle             | 9.17 us                                                     | 8.19 us: 1.12x faster                                                      |
| xml_etree_process    | 43.4 ms                                                     | 39.1 ms: 1.11x faster                                                      |
| xml_etree_parse      | 102 ms                                                      | 96.2 ms: 1.06x faster                                                      |
| json_loads           | 14.2 us                                                     | 13.5 us: 1.05x faster                                                      |
| xml_etree_generate   | 54.5 ms                                                     | 56.9 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 66.3 ms: 1.04x slower                                                      |
| pickle               | 6.80 us                                                     | 7.22 us: 1.06x slower                                                      |
| pickle_dict          | 16.9 us                                                     | 18.4 us: 1.09x slower                                                      |
| pickle_list          | 2.59 us                                                     | 2.89 us: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf1-amd64-python-dba72175116373c1d15e-3.13.0a0-dba7217 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf1-amd64-python-dba72175116373c1d15e-3.13.0a0-dba7217 |
|-----------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.48 ms: 1.18x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-pythonperf1-amd64-python-dba72175116373c1d15e-3.13.0a0-dba7217 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 95.6 us: 3.40x faster                                                      |
| deltablue                | 4.17 ms                                                     | 2.18 ms: 1.91x faster                                                      |
| richards_super           | 51.7 ms                                                     | 31.6 ms: 1.64x faster                                                      |
| mypy2                    | 352 ms                                                      | 218 ms: 1.61x faster                                                       |
| logging_silent           | 96.4 ns                                                     | 60.0 ns: 1.61x faster                                                      |
| richards                 | 41.2 ms                                                     | 26.8 ms: 1.54x faster                                                      |
| go                       | 136 ms                                                      | 89.1 ms: 1.53x faster                                                      |
| json_dumps               | 8.50 ms                                                     | 5.76 ms: 1.48x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 828 us: 1.47x faster                                                       |
| scimark_lu               | 85.4 ms                                                     | 58.8 ms: 1.45x faster                                                      |
| asyncio_tcp              | 712 ms                                                      | 501 ms: 1.42x faster                                                       |
| async_tree_memoization   | 497 ms                                                      | 350 ms: 1.42x faster                                                       |
| raytrace                 | 271 ms                                                      | 191 ms: 1.42x faster                                                       |
| async_tree_io            | 1.07 sec                                                    | 755 ms: 1.41x faster                                                       |
| async_tree_none          | 420 ms                                                      | 298 ms: 1.41x faster                                                       |
| sqlglot_transpile        | 1.46 ms                                                     | 1.04 ms: 1.41x faster                                                      |
| generators               | 31.6 ms                                                     | 22.6 ms: 1.40x faster                                                      |
| chaos                    | 58.9 ms                                                     | 42.7 ms: 1.38x faster                                                      |
| crypto_pyaes             | 62.3 ms                                                     | 45.8 ms: 1.36x faster                                                      |
| hexiom                   | 5.52 ms                                                     | 4.11 ms: 1.34x faster                                                      |
| pickle_pure_python       | 257 us                                                      | 193 us: 1.33x faster                                                       |
| scimark_sor              | 105 ms                                                      | 80.7 ms: 1.30x faster                                                      |
| pyflate                  | 387 ms                                                      | 299 ms: 1.30x faster                                                       |
| scimark_monte_carlo      | 55.9 ms                                                     | 43.2 ms: 1.29x faster                                                      |
| unpickle_pure_python     | 171 us                                                      | 133 us: 1.28x faster                                                       |
| pycparser                | 868 ms                                                      | 707 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 497 ms: 1.22x faster                                                       |
| tornado_http             | 109 ms                                                      | 90.5 ms: 1.20x faster                                                      |
| mdp                      | 1.71 sec                                                    | 1.44 sec: 1.19x faster                                                     |
| deepcopy_memo            | 28.5 us                                                     | 24.1 us: 1.18x faster                                                      |
| spectral_norm            | 78.0 ms                                                     | 66.3 ms: 1.18x faster                                                      |
| mako                     | 8.80 ms                                                     | 7.48 ms: 1.18x faster                                                      |
| regex_compile            | 103 ms                                                      | 88.2 ms: 1.17x faster                                                      |
| docutils                 | 1.89 sec                                                    | 1.64 sec: 1.15x faster                                                     |
| pprint_pformat           | 1.21 sec                                                    | 1.05 sec: 1.15x faster                                                     |
| pprint_safe_repr         | 589 ms                                                      | 516 ms: 1.14x faster                                                       |
| tomli_loads              | 1.62 sec                                                    | 1.43 sec: 1.13x faster                                                     |
| sqlglot_optimize         | 39.0 ms                                                     | 34.6 ms: 1.12x faster                                                      |
| unpickle                 | 9.17 us                                                     | 8.19 us: 1.12x faster                                                      |
| bench_thread_pool        | 946 us                                                      | 848 us: 1.12x faster                                                       |
| xml_etree_process        | 43.4 ms                                                     | 39.1 ms: 1.11x faster                                                      |
| nqueens                  | 67.0 ms                                                     | 60.9 ms: 1.10x faster                                                      |
| sqlglot_normalize        | 202 ms                                                      | 185 ms: 1.09x faster                                                       |
| comprehensions           | 16.0 us                                                     | 14.7 us: 1.09x faster                                                      |
| deepcopy                 | 255 us                                                      | 236 us: 1.08x faster                                                       |
| float                    | 60.2 ms                                                     | 56.3 ms: 1.07x faster                                                      |
| dulwich_log              | 47.6 ms                                                     | 44.6 ms: 1.07x faster                                                      |
| fannkuch                 | 258 ms                                                      | 242 ms: 1.06x faster                                                       |
| regex_dna                | 132 ms                                                      | 124 ms: 1.06x faster                                                       |
| scimark_fft              | 193 ms                                                      | 182 ms: 1.06x faster                                                       |
| sqlite_synth             | 1.84 us                                                     | 1.74 us: 1.06x faster                                                      |
| xml_etree_parse          | 102 ms                                                      | 96.2 ms: 1.06x faster                                                      |
| coroutines               | 15.9 ms                                                     | 15.1 ms: 1.06x faster                                                      |
| create_gc_cycles         | 782 us                                                      | 743 us: 1.05x faster                                                       |
| json_loads               | 14.2 us                                                     | 13.5 us: 1.05x faster                                                      |
| json                     | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.56 ms: 1.04x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.04x faster                                                      |
| deepcopy_reduce          | 2.16 us                                                     | 2.10 us: 1.03x faster                                                      |
| meteor_contest           | 72.5 ms                                                     | 74.7 ms: 1.03x slower                                                      |
| pidigits                 | 145 ms                                                      | 150 ms: 1.04x slower                                                       |
| logging_format           | 6.66 us                                                     | 6.94 us: 1.04x slower                                                      |
| xml_etree_generate       | 54.5 ms                                                     | 56.9 ms: 1.04x slower                                                      |
| xml_etree_iterparse      | 63.5 ms                                                     | 66.3 ms: 1.04x slower                                                      |
| unpack_sequence          | 37.8 ns                                                     | 39.8 ns: 1.05x slower                                                      |
| logging_simple           | 6.20 us                                                     | 6.54 us: 1.06x slower                                                      |
| pickle                   | 6.80 us                                                     | 7.22 us: 1.06x slower                                                      |
| pathlib                  | 77.4 ms                                                     | 83.2 ms: 1.08x slower                                                      |
| telco                    | 3.78 ms                                                     | 4.08 ms: 1.08x slower                                                      |
| nbody                    | 69.3 ms                                                     | 74.9 ms: 1.08x slower                                                      |
| pickle_dict              | 16.9 us                                                     | 18.4 us: 1.09x slower                                                      |
| async_generators         | 224 ms                                                      | 246 ms: 1.10x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.1 ms: 1.10x slower                                                      |
| bench_mp_pool            | 60.7 ms                                                     | 66.9 ms: 1.10x slower                                                      |
| pickle_list              | 2.59 us                                                     | 2.89 us: 1.12x slower                                                      |
| gc_traversal             | 1.34 ms                                                     | 1.52 ms: 1.13x slower                                                      |
| coverage                 | 40.0 ms                                                     | 52.9 ms: 1.32x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (4): regex_v8, unpickle_list, asyncio_tcp_ssl, python_startup
Ignored benchmarks (17) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
