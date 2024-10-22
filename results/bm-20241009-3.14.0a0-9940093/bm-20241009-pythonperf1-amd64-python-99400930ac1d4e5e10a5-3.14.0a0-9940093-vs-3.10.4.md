# Results vs. 3.10.4

- fork: python
- ref: 99400930ac1d4e5e10a5
- machine: windows-amd64
- commit hash: 9940093
- commit date: 2024-10-09
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                     |
| html5lib       | 51.0 ms                                                     | 41.9 ms: 1.22x faster                                                      |
| tornado_http   | 108 ms                                                      | 94.1 ms: 1.15x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 219 ms: 1.99x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 269 ms: 1.96x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 603 ms: 1.84x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 404 ms: 1.58x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.83x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.5 ms: 1.09x faster                                                      |
| nbody          | 71.3 ms                                                     | 85.6 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                       |
| regex_compile  | 106 ms                                                      | 91.8 ms: 1.15x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.41 ms: 1.43x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 220 us: 1.22x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 159 us: 1.15x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 42.5 ms: 1.05x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 95.9 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.0 ms: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.82 us: 1.04x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.92 us: 1.06x slower                                                      |
| pickle               | 6.85 us                                                     | 7.31 us: 1.07x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 59.4 ms: 1.07x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.0 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (2): tomli_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.1 ms: 1.07x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.19 ms: 1.26x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                      |
| django_template | 28.9 ms                                                     | 26.3 ms: 1.10x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 38.3 ms: 1.07x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.95x faster                                                       |
| async_tree_none          | 435 ms                                                      | 219 ms: 1.99x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 269 ms: 1.96x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 603 ms: 1.84x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.33 ms: 1.80x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 404 ms: 1.58x faster                                                       |
| pylint                   | 350 ms                                                      | 230 ms: 1.53x faster                                                       |
| go                       | 139 ms                                                      | 91.7 ms: 1.52x faster                                                      |
| generators               | 32.4 ms                                                     | 22.1 ms: 1.47x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 65.4 ns: 1.45x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.41 ms: 1.43x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.37x faster                                                      |
| richards_super           | 52.2 ms                                                     | 38.1 ms: 1.37x faster                                                      |
| raytrace                 | 273 ms                                                      | 201 ms: 1.36x faster                                                       |
| chaos                    | 61.7 ms                                                     | 45.5 ms: 1.36x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.6 us: 1.33x faster                                                      |
| deepcopy                 | 255 us                                                      | 193 us: 1.32x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 65.3 ms: 1.31x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 936 us: 1.30x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.15 ms: 1.29x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.52 ms: 1.27x faster                                                      |
| richards                 | 42.4 ms                                                     | 33.7 ms: 1.26x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.19 ms: 1.26x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 50.1 ms: 1.25x faster                                                      |
| pycparser                | 930 ms                                                      | 749 ms: 1.24x faster                                                       |
| pyflate                  | 409 ms                                                      | 332 ms: 1.23x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.72 sec: 1.22x faster                                                     |
| pickle_pure_python       | 270 us                                                      | 220 us: 1.22x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 41.9 ms: 1.22x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                                     |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                       |
| thrift                   | 617 us                                                      | 528 us: 1.17x faster                                                       |
| sympy_sum                | 107 ms                                                      | 91.5 ms: 1.17x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.64 us: 1.17x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 827 us: 1.16x faster                                                       |
| regex_compile            | 106 ms                                                      | 91.8 ms: 1.15x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 159 us: 1.15x faster                                                       |
| tornado_http             | 108 ms                                                      | 94.1 ms: 1.15x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 44.2 ms: 1.14x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.4 ms: 1.14x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 652 ms: 1.12x faster                                                       |
| scimark_sor              | 106 ms                                                      | 94.8 ms: 1.12x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.7 ms: 1.12x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.99 us: 1.11x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.3 ms: 1.10x faster                                                      |
| float                    | 61.7 ms                                                     | 56.5 ms: 1.09x faster                                                      |
| sympy_str                | 194 ms                                                      | 179 ms: 1.08x faster                                                       |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 38.3 ms: 1.07x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 37.9 ms: 1.05x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 42.5 ms: 1.05x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 74.6 ms: 1.04x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.18 sec: 1.03x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 575 ms: 1.03x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 200 ms: 1.03x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 65.5 ms: 1.02x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 95.9 ms: 1.01x faster                                                      |
| sympy_expand             | 314 ms                                                      | 312 ms: 1.01x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 39.9 ns: 1.01x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.0 ms: 1.02x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 78.1 ms: 1.03x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.82 us: 1.04x slower                                                      |
| logging_format           | 6.76 us                                                     | 7.02 us: 1.04x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 80.4 ms: 1.06x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.92 us: 1.06x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.62 us: 1.06x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.31 us: 1.07x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 59.4 ms: 1.07x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.1 ms: 1.07x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.53 ms: 1.09x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.0 us: 1.10x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 69.2 ms: 1.11x slower                                                      |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                      |
| scimark_fft              | 187 ms                                                      | 215 ms: 1.15x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 928 us: 1.16x slower                                                       |
| fannkuch                 | 256 ms                                                      | 297 ms: 1.16x slower                                                       |
| nbody                    | 71.3 ms                                                     | 85.6 ms: 1.20x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.90 ms: 1.24x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.7 ms: 1.25x slower                                                      |
| json                     | 3.14 ms                                                     | 4.52 ms: 1.44x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.13x faster                                                               |

Benchmark hidden because not significant (5): tomli_loads, scimark_sparse_mat_mult, pidigits, unpickle, regex_v8
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241009-3.14.0a0-9940093/bm-20241009-pythonperf1-amd64-python-99400930ac1d4e5e10a5-3.14.0a0-9940093.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown