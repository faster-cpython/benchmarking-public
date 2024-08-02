# Results vs. 3.10.4

- fork: python
- ref: a9d56e38a08ec198a228
- machine: windows-amd64
- commit hash: a9d56e3
- commit date: 2024-08-01
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 240 ms: 1.02x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.85 sec: 1.04x faster                                                     |
| html5lib       | 51.0 ms                                                     | 42.0 ms: 1.22x faster                                                      |
| tornado_http   | 108 ms                                                      | 95.5 ms: 1.13x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 212 ms: 2.06x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 545 ms: 2.03x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 261 ms: 2.02x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 393 ms: 1.62x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.92x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 51.5 ms: 1.38x faster                                                      |
| float          | 61.7 ms                                                     | 45.4 ms: 1.36x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.7 ms: 1.16x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.99 ms: 1.53x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 184 us: 1.47x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 137 us: 1.34x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.26 sec: 1.32x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 37.8 ms: 1.18x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 52.3 ms: 1.06x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.5 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.2 ms: 1.04x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 4.97 ms: 1.82x faster                                                      |
| django_template | 28.9 ms                                                     | 25.9 ms: 1.12x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 118 us: 2.85x faster                                                       |
| async_tree_none          | 435 ms                                                      | 212 ms: 2.06x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 545 ms: 2.03x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 261 ms: 2.02x faster                                                       |
| mako                     | 9.03 ms                                                     | 4.97 ms: 1.82x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 16.1 us: 1.79x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.35 ms: 1.78x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 45.8 ms: 1.69x faster                                                      |
| pyflate                  | 409 ms                                                      | 247 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 393 ms: 1.62x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 58.7 ns: 1.61x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.61x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 39.4 ms: 1.59x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.4 ms: 1.57x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.99 ms: 1.53x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.0 ms: 1.51x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.42 sec: 1.49x faster                                                     |
| pickle_pure_python       | 270 us                                                      | 184 us: 1.47x faster                                                       |
| richards_super           | 52.2 ms                                                     | 35.6 ms: 1.47x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 844 us: 1.44x faster                                                       |
| raytrace                 | 273 ms                                                      | 192 ms: 1.42x faster                                                       |
| generators               | 32.4 ms                                                     | 23.0 ms: 1.41x faster                                                      |
| nbody                    | 71.3 ms                                                     | 51.5 ms: 1.38x faster                                                      |
| deepcopy                 | 255 us                                                      | 185 us: 1.38x faster                                                       |
| go                       | 139 ms                                                      | 101 ms: 1.38x faster                                                       |
| pylint                   | 350 ms                                                      | 254 ms: 1.38x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.08 ms: 1.37x faster                                                      |
| float                    | 61.7 ms                                                     | 45.4 ms: 1.36x faster                                                      |
| richards                 | 42.4 ms                                                     | 31.5 ms: 1.35x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 137 us: 1.34x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.26 sec: 1.32x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 555 ms: 1.32x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.07 ms: 1.32x faster                                                      |
| scimark_fft              | 187 ms                                                      | 147 ms: 1.27x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.45 sec: 1.23x faster                                                     |
| pprint_pformat           | 1.22 sec                                                    | 995 ms: 1.23x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 484 ms: 1.22x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 42.0 ms: 1.22x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.82 us: 1.21x faster                                                      |
| fannkuch                 | 256 ms                                                      | 215 ms: 1.19x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.83 ms: 1.19x faster                                                      |
| pycparser                | 930 ms                                                      | 786 ms: 1.18x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 37.8 ms: 1.18x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 814 us: 1.18x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.1 ms: 1.17x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                      |
| thrift                   | 617 us                                                      | 533 us: 1.16x faster                                                       |
| regex_compile            | 106 ms                                                      | 91.7 ms: 1.16x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| scimark_sor              | 106 ms                                                      | 92.7 ms: 1.15x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 75.2 ms: 1.14x faster                                                      |
| tornado_http             | 108 ms                                                      | 95.5 ms: 1.13x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.9 ms: 1.12x faster                                                      |
| sympy_sum                | 107 ms                                                      | 96.3 ms: 1.11x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.8 ms: 1.08x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 70.7 ms: 1.07x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 62.3 ms: 1.07x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 192 ms: 1.07x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 52.3 ms: 1.06x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.5 ms: 1.05x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.2 ms: 1.04x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.7 ms: 1.04x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.85 sec: 1.04x faster                                                     |
| logging_format           | 6.76 us                                                     | 6.53 us: 1.03x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.06 us: 1.03x faster                                                      |
| sympy_str                | 194 ms                                                      | 189 ms: 1.03x faster                                                       |
| 2to3                     | 246 ms                                                      | 240 ms: 1.02x faster                                                       |
| json                     | 3.14 ms                                                     | 3.07 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                      |
| sympy_expand             | 314 ms                                                      | 330 ms: 1.05x slower                                                       |
| python_startup           | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 81.0 ms: 1.07x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.58 ms: 1.12x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 912 us: 1.14x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.54 ms: 1.15x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 73.0 ms: 1.18x slower                                                      |
| async_generators         | 222 ms                                                      | 261 ms: 1.18x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.7 ms: 1.22x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (1): genshi_xml
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240801-3.14.0a0-a9d56e3-JIT/bm-20240801-pythonperf1-amd64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown