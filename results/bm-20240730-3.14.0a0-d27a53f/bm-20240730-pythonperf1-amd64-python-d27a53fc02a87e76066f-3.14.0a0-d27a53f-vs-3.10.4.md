# Results vs. 3.10.4

- fork: python
- ref: d27a53fc02a87e76066f
- machine: windows-amd64
- commit hash: d27a53f
- commit date: 2024-07-30
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 232 ms: 1.06x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                     |
| html5lib       | 51.0 ms                                                     | 42.1 ms: 1.21x faster                                                      |
| tornado_http   | 108 ms                                                      | 93.6 ms: 1.16x faster                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 264 ms: 2.00x faster                                                       |
| async_tree_none         | 435 ms                                                      | 221 ms: 1.97x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 581 ms: 1.91x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 389 ms: 1.64x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.4 ms: 1.09x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 85.8 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 93.3 ms: 1.14x faster                                                      |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 17.4 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.31 ms: 1.45x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 217 us: 1.24x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 152 us: 1.20x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 42.2 ms: 1.05x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 93.1 ms: 1.04x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.6 ms: 1.01x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 58.8 ms: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.40 ms: 1.22x faster                                                      |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.0 ms: 1.10x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 39.5 ms: 1.04x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 116 us: 2.90x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 264 ms: 2.00x faster                                                       |
| async_tree_none          | 435 ms                                                      | 221 ms: 1.97x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 581 ms: 1.91x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.31 ms: 1.81x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 389 ms: 1.64x faster                                                       |
| pylint                   | 350 ms                                                      | 229 ms: 1.53x faster                                                       |
| generators               | 32.4 ms                                                     | 21.2 ms: 1.53x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 64.4 ns: 1.47x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.31 ms: 1.45x faster                                                      |
| richards_super           | 52.2 ms                                                     | 37.5 ms: 1.39x faster                                                      |
| go                       | 139 ms                                                      | 99.8 ms: 1.39x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.53 sec: 1.38x faster                                                     |
| chaos                    | 61.7 ms                                                     | 45.0 ms: 1.37x faster                                                      |
| raytrace                 | 273 ms                                                      | 202 ms: 1.35x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.3 us: 1.35x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 544 ms: 1.35x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 913 us: 1.33x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.4 us: 1.33x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.31x faster                                                      |
| deepcopy                 | 255 us                                                      | 196 us: 1.31x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 66.4 ms: 1.29x faster                                                      |
| richards                 | 42.4 ms                                                     | 33.1 ms: 1.28x faster                                                      |
| pyflate                  | 409 ms                                                      | 325 ms: 1.26x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.61 ms: 1.25x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 217 us: 1.24x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.40 ms: 1.22x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 42.1 ms: 1.21x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                                     |
| crypto_pyaes             | 62.5 ms                                                     | 51.9 ms: 1.20x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 152 us: 1.20x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 804 us: 1.19x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.9 ms: 1.18x faster                                                      |
| sympy_sum                | 107 ms                                                      | 92.0 ms: 1.16x faster                                                      |
| tornado_http             | 108 ms                                                      | 93.6 ms: 1.16x faster                                                      |
| scimark_sor              | 106 ms                                                      | 92.2 ms: 1.15x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.14x faster                                                      |
| thrift                   | 617 us                                                      | 541 us: 1.14x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                      |
| regex_compile            | 106 ms                                                      | 93.3 ms: 1.14x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 18.0 ms: 1.10x faster                                                      |
| float                    | 61.7 ms                                                     | 56.4 ms: 1.09x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 52.6 ms: 1.09x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.03 us: 1.09x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 36.8 ms: 1.08x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 71.8 ms: 1.08x faster                                                      |
| sympy_str                | 194 ms                                                      | 182 ms: 1.07x faster                                                       |
| 2to3                     | 246 ms                                                      | 232 ms: 1.06x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 42.2 ms: 1.05x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 63.4 ms: 1.05x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 197 ms: 1.04x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.17 sec: 1.04x faster                                                     |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.1 ms: 1.04x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 39.5 ms: 1.04x faster                                                      |
| json                     | 3.14 ms                                                     | 3.03 ms: 1.04x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 574 ms: 1.03x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| sympy_expand             | 314 ms                                                      | 310 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.6 ms: 1.01x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.37 us: 1.02x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.92 us: 1.02x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 77.9 ms: 1.03x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.85 ms: 1.05x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 58.8 ms: 1.06x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 80.6 ms: 1.07x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 69.4 ms: 1.12x slower                                                      |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 17.4 ms: 1.12x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 902 us: 1.13x slower                                                       |
| scimark_fft              | 187 ms                                                      | 212 ms: 1.13x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                      |
| fannkuch                 | 256 ms                                                      | 298 ms: 1.17x slower                                                       |
| nbody                    | 71.3 ms                                                     | 85.8 ms: 1.20x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.4 ms: 1.27x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.06 ms: 1.28x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (1): pycparser
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240730-3.14.0a0-d27a53f/bm-20240730-pythonperf1-amd64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown