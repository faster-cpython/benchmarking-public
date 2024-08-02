# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-amd64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 210 ms: 1.17x faster                                                       |
| chameleon      | 5.79 ms                                                     | 4.81 ms: 1.20x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                     |
| html5lib       | 51.0 ms                                                     | 35.2 ms: 1.45x faster                                                      |
| tornado_http   | 108 ms                                                      | 81.6 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.26x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 269 ms: 1.96x faster                                                       |
| async_tree_none         | 435 ms                                                      | 225 ms: 1.93x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 600 ms: 1.85x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 393 ms: 1.62x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.83x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 50.5 ms: 1.22x faster                                                      |
| nbody          | 71.3 ms                                                     | 68.7 ms: 1.04x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 76.7 ms: 1.38x faster                                                      |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.5 ms: 1.07x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.77 ms: 1.59x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 177 us: 1.52x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 126 us: 1.45x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 36.6 ms: 1.21x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 91.8 ms: 1.06x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.73 us: 1.04x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 53.7 ms: 1.03x faster                                                      |
| json_loads           | 14.0 us                                                     | 13.7 us: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.85 us: 1.05x slower                                                      |
| pickle               | 6.85 us                                                     | 7.23 us: 1.06x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.3 us: 1.06x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.26 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.0 ms: 1.02x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 16.6 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.41 ms: 1.41x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 14.6 ms: 1.36x faster                                                      |
| django_template | 28.9 ms                                                     | 21.9 ms: 1.32x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 31.5 ms: 1.30x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.35x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 99.8 us: 3.37x faster                                                      |
| deltablue                | 4.19 ms                                                     | 1.90 ms: 2.20x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 269 ms: 1.96x faster                                                       |
| async_tree_none          | 435 ms                                                      | 225 ms: 1.93x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 600 ms: 1.85x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.1 ns: 1.75x faster                                                      |
| raytrace                 | 273 ms                                                      | 157 ms: 1.74x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.6 ms: 1.71x faster                                                      |
| pylint                   | 350 ms                                                      | 208 ms: 1.68x faster                                                       |
| go                       | 139 ms                                                      | 83.5 ms: 1.66x faster                                                      |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.64x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 393 ms: 1.62x faster                                                       |
| chaos                    | 61.7 ms                                                     | 38.3 ms: 1.61x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 762 us: 1.59x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.77 ms: 1.59x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.58x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 470 ms: 1.56x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 966 us: 1.53x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 177 us: 1.52x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.81 ms: 1.51x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 58.1 ms: 1.48x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.45 sec: 1.46x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 126 us: 1.45x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 35.2 ms: 1.45x faster                                                      |
| pyflate                  | 409 ms                                                      | 284 ms: 1.44x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.41 ms: 1.41x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.2 ms: 1.39x faster                                                      |
| regex_compile            | 106 ms                                                      | 76.7 ms: 1.38x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 45.9 ms: 1.36x faster                                                      |
| pycparser                | 930 ms                                                      | 684 ms: 1.36x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 14.6 ms: 1.36x faster                                                      |
| scimark_sor              | 106 ms                                                      | 78.5 ms: 1.35x faster                                                      |
| tornado_http             | 108 ms                                                      | 81.6 ms: 1.33x faster                                                      |
| django_template          | 28.9 ms                                                     | 21.9 ms: 1.32x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 31.5 ms: 1.30x faster                                                      |
| sympy_sum                | 107 ms                                                      | 83.6 ms: 1.28x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 22.5 us: 1.28x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.41 sec: 1.26x faster                                                     |
| coroutines               | 16.0 ms                                                     | 12.8 ms: 1.25x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                                      |
| thrift                   | 617 us                                                      | 501 us: 1.23x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                     |
| pprint_pformat           | 1.22 sec                                                    | 997 ms: 1.22x faster                                                       |
| float                    | 61.7 ms                                                     | 50.5 ms: 1.22x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.6 ms: 1.21x faster                                                      |
| sympy_str                | 194 ms                                                      | 160 ms: 1.21x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 492 ms: 1.20x faster                                                       |
| chameleon                | 5.79 ms                                                     | 4.81 ms: 1.20x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 33.3 ms: 1.20x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 802 us: 1.19x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 64.7 ms: 1.19x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                     |
| sqlglot_normalize        | 205 ms                                                      | 175 ms: 1.17x faster                                                       |
| 2to3                     | 246 ms                                                      | 210 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 57.4 ms: 1.16x faster                                                      |
| deepcopy                 | 255 us                                                      | 220 us: 1.16x faster                                                       |
| sympy_expand             | 314 ms                                                      | 272 ms: 1.16x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.00 us: 1.10x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.51 ms: 1.09x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.26 us: 1.08x faster                                                      |
| json                     | 3.14 ms                                                     | 2.92 ms: 1.07x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.80 us: 1.07x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.5 ms: 1.07x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 71.5 ms: 1.06x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 91.8 ms: 1.06x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.73 us: 1.04x faster                                                      |
| nbody                    | 71.3 ms                                                     | 68.7 ms: 1.04x faster                                                      |
| scimark_fft              | 187 ms                                                      | 181 ms: 1.04x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 53.7 ms: 1.03x faster                                                      |
| fannkuch                 | 256 ms                                                      | 249 ms: 1.03x faster                                                       |
| json_loads               | 14.0 us                                                     | 13.7 us: 1.03x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.3 ms: 1.03x faster                                                      |
| async_generators         | 222 ms                                                      | 223 ms: 1.01x slower                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| python_startup           | 20.6 ms                                                     | 21.0 ms: 1.02x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 78.7 ms: 1.04x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.85 us: 1.05x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.23 us: 1.06x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.3 us: 1.06x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 66.2 ms: 1.07x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 16.6 ms: 1.07x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.11x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 916 us: 1.14x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.26 us: 1.18x slower                                                      |
| coverage                 | 39.0 ms                                                     | 46.3 ms: 1.19x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.70 ms: 1.19x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                               |

Benchmark hidden because not significant (1): flaskblogging
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown