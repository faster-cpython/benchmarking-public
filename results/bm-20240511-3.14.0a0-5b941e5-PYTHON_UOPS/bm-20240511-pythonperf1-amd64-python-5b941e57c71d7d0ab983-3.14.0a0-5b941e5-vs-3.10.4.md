# Results vs. 3.10.4

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-amd64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.12x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 237 ms: 1.04x faster                                                       |
| chameleon      | 5.79 ms                                                     | 5.39 ms: 1.07x faster                                                      |
| docutils       | 1.92 sec                                                    | 1.85 sec: 1.04x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.9 ms: 1.25x faster                                                      |
| tornado_http   | 108 ms                                                      | 87.9 ms: 1.23x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 285 ms: 1.85x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 599 ms: 1.85x faster                                                       |
| async_tree_none         | 435 ms                                                      | 238 ms: 1.83x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 407 ms: 1.57x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.77x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 54.6 ms: 1.13x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 75.7 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.9 ms: 1.03x faster                                                      |
| regex_compile  | 106 ms                                                      | 112 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.76 ms: 1.59x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 228 us: 1.18x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 40.3 ms: 1.10x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 167 us: 1.09x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.55 sec: 1.08x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 90.1 ms: 1.07x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.55 us: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.4 ms: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.80 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.4 ms: 1.03x slower                                                      |
| pickle               | 6.85 us                                                     | 7.13 us: 1.04x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.3 us: 1.06x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.11 us: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 20.3 ms: 1.01x faster                                                      |
| python_startup_no_site | 15.5 ms                                                     | 16.5 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.85 ms: 1.15x faster                                                      |
| django_template | 28.9 ms                                                     | 25.2 ms: 1.15x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 37.0 ms: 1.11x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 116 us: 2.90x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 285 ms: 1.85x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 599 ms: 1.85x faster                                                       |
| async_tree_none          | 435 ms                                                      | 238 ms: 1.83x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.76 ms: 1.59x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 407 ms: 1.57x faster                                                       |
| generators               | 32.4 ms                                                     | 20.7 ms: 1.56x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.75 ms: 1.52x faster                                                      |
| richards_super           | 52.2 ms                                                     | 34.7 ms: 1.51x faster                                                      |
| pylint                   | 350 ms                                                      | 235 ms: 1.49x faster                                                       |
| raytrace                 | 273 ms                                                      | 190 ms: 1.43x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.53 sec: 1.38x faster                                                     |
| richards                 | 42.4 ms                                                     | 30.9 ms: 1.37x faster                                                      |
| chaos                    | 61.7 ms                                                     | 45.6 ms: 1.35x faster                                                      |
| go                       | 139 ms                                                      | 104 ms: 1.34x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 919 us: 1.32x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 572 ms: 1.28x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.16 ms: 1.27x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.9 ms: 1.25x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 76.5 ns: 1.24x faster                                                      |
| coroutines               | 16.0 ms                                                     | 12.9 ms: 1.24x faster                                                      |
| tornado_http             | 108 ms                                                      | 87.9 ms: 1.23x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                                     |
| pyflate                  | 409 ms                                                      | 343 ms: 1.19x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 228 us: 1.18x faster                                                       |
| pycparser                | 930 ms                                                      | 788 ms: 1.18x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 53.1 ms: 1.18x faster                                                      |
| thrift                   | 617 us                                                      | 527 us: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.17x faster                                                      |
| comprehensions           | 16.5 us                                                     | 14.3 us: 1.15x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.85 ms: 1.15x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.2 ms: 1.15x faster                                                      |
| scimark_sor              | 106 ms                                                      | 92.5 ms: 1.15x faster                                                      |
| float                    | 61.7 ms                                                     | 54.6 ms: 1.13x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.8 ms: 1.11x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 861 us: 1.11x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 37.0 ms: 1.11x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 40.3 ms: 1.10x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 167 us: 1.09x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 52.7 ms: 1.09x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.55 sec: 1.08x faster                                                     |
| xml_etree_parse          | 96.8 ms                                                     | 90.1 ms: 1.07x faster                                                      |
| chameleon                | 5.79 ms                                                     | 5.39 ms: 1.07x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.55 us: 1.06x faster                                                      |
| sympy_sum                | 107 ms                                                      | 101 ms: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 81.6 ms: 1.05x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.17 sec: 1.04x faster                                                     |
| docutils                 | 1.92 sec                                                    | 1.85 sec: 1.04x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 570 ms: 1.04x faster                                                       |
| 2to3                     | 246 ms                                                      | 237 ms: 1.04x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.9 ms: 1.03x faster                                                      |
| json                     | 3.14 ms                                                     | 3.03 ms: 1.03x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.9 ms: 1.03x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 39.1 ms: 1.02x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.65 us: 1.02x faster                                                      |
| python_startup           | 20.6 ms                                                     | 20.3 ms: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| sympy_str                | 194 ms                                                      | 198 ms: 1.02x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.4 ms: 1.02x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 78.1 ms: 1.03x slower                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.27 us: 1.03x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.80 us: 1.03x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.4 ms: 1.03x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.13 us: 1.04x slower                                                      |
| deepcopy                 | 255 us                                                      | 266 us: 1.04x slower                                                       |
| regex_compile            | 106 ms                                                      | 112 ms: 1.05x slower                                                       |
| spectral_norm            | 77.3 ms                                                     | 81.6 ms: 1.06x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 80.0 ms: 1.06x slower                                                      |
| nbody                    | 71.3 ms                                                     | 75.7 ms: 1.06x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.3 us: 1.06x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 16.5 ms: 1.07x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 71.2 ms: 1.07x slower                                                      |
| sympy_expand             | 314 ms                                                      | 338 ms: 1.08x slower                                                       |
| deepcopy_memo            | 28.8 us                                                     | 31.2 us: 1.09x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 68.5 ms: 1.10x slower                                                      |
| scimark_fft              | 187 ms                                                      | 207 ms: 1.11x slower                                                       |
| async_generators         | 222 ms                                                      | 247 ms: 1.11x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.12x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 896 us: 1.12x slower                                                       |
| fannkuch                 | 256 ms                                                      | 289 ms: 1.13x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.11 us: 1.13x slower                                                      |
| coverage                 | 39.0 ms                                                     | 46.0 ms: 1.18x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.29 ms: 1.21x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.84 ms: 1.23x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (4): json_loads, logging_simple, flaskblogging, hexiom
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240511-3.14.0a0-5b941e5-PYTHON_UOPS/bm-20240511-pythonperf1-amd64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown