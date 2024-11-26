# Results vs. 3.10.4

- fork: python
- ref: b3aa1b5fe260382788a2
- machine: windows-amd64
- commit hash: b3aa1b5
- commit date: 2024-10-11
- overall geometric mean: 1.172x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 229 ms: 1.07x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.72 sec: 1.11x faster                                                     |
| html5lib       | 51.0 ms                                                     | 42.9 ms: 1.19x faster                                                      |
| tornado_http   | 108 ms                                                      | 94.9 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 214 ms: 2.03x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 272 ms: 1.94x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 591 ms: 1.88x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 396 ms: 1.61x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.86x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 53.8 ms: 1.15x faster                                                      |
| nbody          | 71.3 ms                                                     | 79.3 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.3 ms: 1.16x faster                                                      |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.75 ms: 1.36x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 220 us: 1.23x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 40.2 ms: 1.11x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.64 sec: 1.02x faster                                                     |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.3 ms: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.80 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.4 ms: 1.03x slower                                                      |
| unpickle             | 9.09 us                                                     | 9.40 us: 1.03x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                                      |
| pickle               | 6.85 us                                                     | 7.25 us: 1.06x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.95 us: 1.07x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.2 us: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.78 ms: 1.33x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                      |
| django_template | 28.9 ms                                                     | 25.7 ms: 1.12x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 37.0 ms: 1.11x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.01x faster                                                       |
| async_tree_none          | 435 ms                                                      | 214 ms: 2.03x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 272 ms: 1.94x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 591 ms: 1.88x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 396 ms: 1.61x faster                                                       |
| go                       | 139 ms                                                      | 86.4 ms: 1.61x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 60.7 ns: 1.56x faster                                                      |
| pylint                   | 350 ms                                                      | 230 ms: 1.52x faster                                                       |
| generators               | 32.4 ms                                                     | 21.5 ms: 1.50x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 58.4 ms: 1.47x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 19.7 us: 1.46x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.2 ms: 1.44x faster                                                      |
| chaos                    | 61.7 ms                                                     | 43.7 ms: 1.41x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.40x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.75 ms: 1.36x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 908 us: 1.34x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.78 ms: 1.33x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.33 ms: 1.33x faster                                                      |
| deepcopy                 | 255 us                                                      | 193 us: 1.32x faster                                                       |
| richards                 | 42.4 ms                                                     | 32.1 ms: 1.32x faster                                                      |
| raytrace                 | 273 ms                                                      | 207 ms: 1.32x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 48.1 ms: 1.30x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.14 ms: 1.30x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 568 ms: 1.29x faster                                                       |
| pyflate                  | 409 ms                                                      | 318 ms: 1.28x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.65 sec: 1.28x faster                                                     |
| pycparser                | 930 ms                                                      | 743 ms: 1.25x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 46.7 ms: 1.23x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 220 us: 1.23x faster                                                       |
| scimark_sor              | 106 ms                                                      | 88.2 ms: 1.20x faster                                                      |
| thrift                   | 617 us                                                      | 516 us: 1.20x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 42.9 ms: 1.19x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 812 us: 1.18x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.9 ms: 1.18x faster                                                      |
| regex_compile            | 106 ms                                                      | 91.3 ms: 1.16x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.55 sec: 1.15x faster                                                     |
| float                    | 61.7 ms                                                     | 53.8 ms: 1.15x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.67 us: 1.15x faster                                                      |
| tornado_http             | 108 ms                                                      | 94.9 ms: 1.14x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 44.5 ms: 1.13x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 68.3 ms: 1.13x faster                                                      |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.7 ms: 1.12x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.72 sec: 1.11x faster                                                     |
| genshi_xml               | 41.0 ms                                                     | 37.0 ms: 1.11x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 40.2 ms: 1.11x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.00 us: 1.10x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 36.0 ns: 1.10x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                     |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 547 ms: 1.08x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.9 ms: 1.08x faster                                                      |
| 2to3                     | 246 ms                                                      | 229 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 196 ms: 1.05x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 64.4 ms: 1.03x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.64 sec: 1.02x faster                                                     |
| sympy_expand             | 314 ms                                                      | 309 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.68 ms: 1.02x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 76.6 ms: 1.01x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.85 us: 1.01x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.3 ms: 1.02x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.38 us: 1.03x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.80 us: 1.03x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.4 ms: 1.03x slower                                                      |
| unpickle                 | 9.09 us                                                     | 9.40 us: 1.03x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.25 us: 1.06x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 80.4 ms: 1.06x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.95 us: 1.07x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.3 ms: 1.08x slower                                                      |
| scimark_fft              | 187 ms                                                      | 203 ms: 1.08x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.53 ms: 1.09x slower                                                      |
| fannkuch                 | 256 ms                                                      | 282 ms: 1.10x slower                                                       |
| nbody                    | 71.3 ms                                                     | 79.3 ms: 1.11x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 69.3 ms: 1.12x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.2 us: 1.12x slower                                                      |
| async_generators         | 222 ms                                                      | 249 ms: 1.12x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 923 us: 1.15x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                                      |
| coverage                 | 39.0 ms                                                     | 46.6 ms: 1.20x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.83 ms: 1.23x slower                                                      |
| json                     | 3.14 ms                                                     | 4.18 ms: 1.33x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, pidigits
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241011-3.14.0a0-b3aa1b5/bm-20241011-pythonperf1-amd64-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.172x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown