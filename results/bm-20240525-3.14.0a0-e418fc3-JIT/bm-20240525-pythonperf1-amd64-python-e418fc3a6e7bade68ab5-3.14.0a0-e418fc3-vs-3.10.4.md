# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-amd64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| chameleon      | 5.79 ms                                                     | 5.14 ms: 1.13x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.5 ms: 1.36x faster                                                      |
| tornado_http   | 108 ms                                                      | 85.3 ms: 1.27x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 228 ms: 1.91x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 281 ms: 1.87x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 603 ms: 1.84x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 401 ms: 1.59x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.80x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                      |
| nbody          | 71.3 ms                                                     | 51.2 ms: 1.39x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.5 ms: 1.21x faster                                                      |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.75 ms: 1.59x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 170 us: 1.59x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 125 us: 1.46x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 36.0 ms: 1.24x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.9 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.1 ms: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.3 ms: 1.05x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.96 us: 1.01x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 17.5 us: 1.02x slower                                                      |
| pickle               | 6.85 us                                                     | 7.08 us: 1.03x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.87 us: 1.04x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.92 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.8 ms: 1.11x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.8 ms: 1.22x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 4.90 ms: 1.84x faster                                                      |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.2 ms: 1.09x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 44.8 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.91x faster                                                       |
| async_tree_none          | 435 ms                                                      | 228 ms: 1.91x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 281 ms: 1.87x faster                                                       |
| mako                     | 9.03 ms                                                     | 4.90 ms: 1.84x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 603 ms: 1.84x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.35 ms: 1.78x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 54.5 ns: 1.74x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 46.1 ms: 1.67x faster                                                      |
| richards_super           | 52.2 ms                                                     | 32.3 ms: 1.62x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.61x faster                                                      |
| pyflate                  | 409 ms                                                      | 256 ms: 1.60x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.75 ms: 1.59x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 401 ms: 1.59x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 170 us: 1.59x faster                                                       |
| raytrace                 | 273 ms                                                      | 175 ms: 1.56x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.37 sec: 1.54x faster                                                     |
| chaos                    | 61.7 ms                                                     | 40.3 ms: 1.53x faster                                                      |
| generators               | 32.4 ms                                                     | 21.2 ms: 1.52x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 41.4 ms: 1.51x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 805 us: 1.51x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 487 ms: 1.50x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.3 ms: 1.50x faster                                                      |
| pylint                   | 350 ms                                                      | 236 ms: 1.48x faster                                                       |
| go                       | 139 ms                                                      | 93.7 ms: 1.48x faster                                                      |
| richards                 | 42.4 ms                                                     | 28.7 ms: 1.48x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 125 us: 1.46x faster                                                       |
| float                    | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.04 ms: 1.42x faster                                                      |
| nbody                    | 71.3 ms                                                     | 51.2 ms: 1.39x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.7 us: 1.39x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                     |
| html5lib                 | 51.0 ms                                                     | 37.5 ms: 1.36x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 935 ms: 1.30x faster                                                       |
| scimark_sor              | 106 ms                                                      | 81.5 ms: 1.30x faster                                                      |
| pycparser                | 930 ms                                                      | 721 ms: 1.29x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 461 ms: 1.28x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.14 ms: 1.27x faster                                                      |
| tornado_http             | 108 ms                                                      | 85.3 ms: 1.27x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 67.7 ms: 1.27x faster                                                      |
| scimark_fft              | 187 ms                                                      | 149 ms: 1.25x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.0 ms: 1.24x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.45 sec: 1.23x faster                                                     |
| hexiom                   | 5.74 ms                                                     | 4.67 ms: 1.23x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.1 ms: 1.22x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                      |
| regex_compile            | 106 ms                                                      | 87.5 ms: 1.21x faster                                                      |
| thrift                   | 617 us                                                      | 513 us: 1.20x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 826 us: 1.16x faster                                                       |
| sympy_sum                | 107 ms                                                      | 92.4 ms: 1.16x faster                                                      |
| fannkuch                 | 256 ms                                                      | 221 ms: 1.16x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| chameleon                | 5.79 ms                                                     | 5.14 ms: 1.13x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.9 ms: 1.10x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.15 us: 1.10x faster                                                      |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 18.2 ms: 1.09x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 50.9 ms: 1.09x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 36.8 ms: 1.08x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.76 us: 1.08x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 62.0 ms: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.94 ms: 1.06x faster                                                      |
| deepcopy                 | 255 us                                                      | 240 us: 1.06x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.1 ms: 1.06x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.3 ms: 1.05x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 73.2 ms: 1.04x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.15 us: 1.02x faster                                                      |
| sympy_expand             | 314 ms                                                      | 309 ms: 1.02x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.96 us: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.00x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 17.5 us: 1.02x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.08 us: 1.03x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 78.8 ms: 1.04x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.87 us: 1.04x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.92 us: 1.07x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 44.8 ms: 1.09x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.8 ms: 1.11x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 911 us: 1.14x slower                                                       |
| async_generators         | 222 ms                                                      | 253 ms: 1.14x slower                                                       |
| coverage                 | 39.0 ms                                                     | 45.3 ms: 1.16x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.62 ms: 1.17x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 73.8 ms: 1.19x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.8 ms: 1.22x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (3): regex_v8, 2to3, flaskblogging
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1-amd64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown