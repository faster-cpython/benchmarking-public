# Results vs. 3.10.4

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-amd64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| html5lib       | 51.0 ms                                                     | 41.4 ms: 1.23x faster                                                      |
| tornado_http   | 108 ms                                                      | 84.6 ms: 1.28x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 213 ms: 2.04x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 265 ms: 1.99x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 578 ms: 1.92x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 389 ms: 1.64x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.89x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.8 ms: 1.11x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 85.0 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| regex_compile  | 106 ms                                                      | 92.6 ms: 1.14x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.16 ms: 1.49x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 218 us: 1.24x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 155 us: 1.18x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.0 ms: 1.08x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 93.5 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.75 us: 1.01x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 58.0 ms: 1.05x slower                                                      |
| unpickle             | 9.09 us                                                     | 9.51 us: 1.05x slower                                                      |
| pickle               | 6.85 us                                                     | 7.19 us: 1.05x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.5 us: 1.08x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.99 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.11 ms: 1.27x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.0 ms: 1.17x faster                                                      |
| django_template | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.02x faster                                                       |
| async_tree_none          | 435 ms                                                      | 213 ms: 2.04x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 265 ms: 1.99x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 578 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.30 ms: 1.82x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 389 ms: 1.64x faster                                                       |
| go                       | 139 ms                                                      | 87.6 ms: 1.59x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 467 ms: 1.57x faster                                                       |
| pylint                   | 350 ms                                                      | 225 ms: 1.55x faster                                                       |
| generators               | 32.4 ms                                                     | 21.2 ms: 1.53x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 63.4 ns: 1.49x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.16 ms: 1.49x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.1 ms: 1.45x faster                                                      |
| chaos                    | 61.7 ms                                                     | 44.2 ms: 1.40x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 61.7 ms: 1.39x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                      |
| raytrace                 | 273 ms                                                      | 201 ms: 1.36x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 896 us: 1.36x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.5 us: 1.34x faster                                                      |
| deepcopy                 | 255 us                                                      | 193 us: 1.33x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.32x faster                                                      |
| richards                 | 42.4 ms                                                     | 32.1 ms: 1.32x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.46 ms: 1.29x faster                                                      |
| tornado_http             | 108 ms                                                      | 84.6 ms: 1.28x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 49.2 ms: 1.27x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.11 ms: 1.27x faster                                                      |
| pyflate                  | 409 ms                                                      | 322 ms: 1.27x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.68 sec: 1.26x faster                                                     |
| pycparser                | 930 ms                                                      | 747 ms: 1.25x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 218 us: 1.24x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 41.4 ms: 1.23x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.45 sec: 1.22x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 155 us: 1.18x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 811 us: 1.18x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.7 ms: 1.18x faster                                                      |
| thrift                   | 617 us                                                      | 525 us: 1.18x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.2 ms: 1.17x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.0 ms: 1.17x faster                                                      |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                      |
| scimark_sor              | 106 ms                                                      | 92.5 ms: 1.15x faster                                                      |
| regex_compile            | 106 ms                                                      | 92.6 ms: 1.14x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.94 us: 1.14x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.6 ms: 1.13x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                     |
| float                    | 61.7 ms                                                     | 55.8 ms: 1.11x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 70.5 ms: 1.10x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.4 ms: 1.09x faster                                                      |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                     |
| sympy_str                | 194 ms                                                      | 179 ms: 1.08x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 41.0 ms: 1.08x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 548 ms: 1.08x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 192 ms: 1.07x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                     |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.5 ms: 1.04x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 64.4 ms: 1.03x faster                                                      |
| sympy_expand             | 314 ms                                                      | 310 ms: 1.01x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.75 us: 1.01x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.91 us: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.42 us: 1.03x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 78.4 ms: 1.03x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 58.0 ms: 1.05x slower                                                      |
| unpickle                 | 9.09 us                                                     | 9.51 us: 1.05x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.19 us: 1.05x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 66.4 ms: 1.07x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.93 ms: 1.08x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.5 us: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.53 ms: 1.09x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.99 us: 1.09x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 43.1 ns: 1.09x slower                                                      |
| async_generators         | 222 ms                                                      | 245 ms: 1.10x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 884 us: 1.11x slower                                                       |
| scimark_fft              | 187 ms                                                      | 212 ms: 1.13x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.1 ms: 1.17x slower                                                      |
| fannkuch                 | 256 ms                                                      | 300 ms: 1.17x slower                                                       |
| nbody                    | 71.3 ms                                                     | 85.0 ms: 1.19x slower                                                      |
| coverage                 | 39.0 ms                                                     | 47.3 ms: 1.21x slower                                                      |
| json                     | 3.14 ms                                                     | 4.04 ms: 1.29x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.39 ms: 1.37x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown