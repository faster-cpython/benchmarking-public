# Results vs. 3.10.4

- fork: zooba
- ref: cfg
- machine: windows-amd64
- commit hash: 7466cb2
- commit date: 2024-05-20
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 215 ms: 1.14x faster                                     |
| chameleon      | 5.79 ms                                                     | 5.03 ms: 1.15x faster                                    |
| docutils       | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                   |
| html5lib       | 51.0 ms                                                     | 39.1 ms: 1.30x faster                                    |
| tornado_http   | 108 ms                                                      | 86.1 ms: 1.26x faster                                    |
| Geometric mean | (ref)                                                       | 1.19x faster                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 282 ms: 1.87x faster                                     |
| async_tree_none         | 435 ms                                                      | 234 ms: 1.86x faster                                     |
| async_tree_io           | 1.11 sec                                                    | 618 ms: 1.79x faster                                     |
| async_tree_cpu_io_mixed | 638 ms                                                      | 420 ms: 1.52x faster                                     |
| Geometric mean          | (ref)                                                       | 1.75x faster                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.6 ms: 1.11x faster                                    |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                     |
| nbody          | 71.3 ms                                                     | 72.4 ms: 1.02x slower                                    |
| Geometric mean | (ref)                                                       | 1.03x faster                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.5 ms: 1.24x faster                                    |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                     |
| regex_v8       | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                    |
| Geometric mean | (ref)                                                       | 1.10x faster                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.08 ms: 1.51x faster                                    |
| pickle_pure_python   | 270 us                                                      | 192 us: 1.40x faster                                     |
| unpickle_pure_python | 183 us                                                      | 137 us: 1.34x faster                                     |
| tomli_loads          | 1.67 sec                                                    | 1.46 sec: 1.14x faster                                   |
| xml_etree_process    | 44.5 ms                                                     | 39.7 ms: 1.12x faster                                    |
| xml_etree_generate   | 55.5 ms                                                     | 58.2 ms: 1.05x slower                                    |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.05x slower                                    |
| pickle               | 6.85 us                                                     | 7.23 us: 1.06x slower                                    |
| unpickle_list        | 2.71 us                                                     | 2.90 us: 1.07x slower                                    |
| xml_etree_parse      | 96.8 ms                                                     | 104 ms: 1.07x slower                                     |
| pickle_dict          | 17.2 us                                                     | 18.7 us: 1.09x slower                                    |
| xml_etree_iterparse  | 65.0 ms                                                     | 70.9 ms: 1.09x slower                                    |
| pickle_list          | 2.75 us                                                     | 3.14 us: 1.14x slower                                    |
| Geometric mean       | (ref)                                                       | 1.05x faster                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.7 ms: 1.05x slower                                    |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                    |
| Geometric mean         | (ref)                                                       | 1.10x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.96 ms: 1.30x faster                                    |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                    |
| django_template | 28.9 ms                                                     | 23.0 ms: 1.26x faster                                    |
| genshi_xml      | 41.0 ms                                                     | 32.8 ms: 1.25x faster                                    |
| Geometric mean  | (ref)                                                       | 1.27x faster                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 109 us: 3.08x faster                                     |
| deltablue                | 4.19 ms                                                     | 2.07 ms: 2.02x faster                                    |
| async_tree_memoization   | 526 ms                                                      | 282 ms: 1.87x faster                                     |
| async_tree_none          | 435 ms                                                      | 234 ms: 1.86x faster                                     |
| async_tree_io            | 1.11 sec                                                    | 618 ms: 1.79x faster                                     |
| richards_super           | 52.2 ms                                                     | 31.5 ms: 1.66x faster                                    |
| raytrace                 | 273 ms                                                      | 166 ms: 1.64x faster                                     |
| logging_silent           | 94.6 ns                                                     | 58.1 ns: 1.63x faster                                    |
| go                       | 139 ms                                                      | 85.9 ms: 1.62x faster                                    |
| generators               | 32.4 ms                                                     | 20.1 ms: 1.61x faster                                    |
| pylint                   | 350 ms                                                      | 218 ms: 1.61x faster                                     |
| chaos                    | 61.7 ms                                                     | 39.5 ms: 1.56x faster                                    |
| sqlglot_parse            | 1.22 ms                                                     | 792 us: 1.53x faster                                     |
| asyncio_tcp              | 732 ms                                                      | 478 ms: 1.53x faster                                     |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 420 ms: 1.52x faster                                     |
| richards                 | 42.4 ms                                                     | 28.1 ms: 1.51x faster                                    |
| json_dumps               | 9.16 ms                                                     | 6.08 ms: 1.51x faster                                    |
| comprehensions           | 16.5 us                                                     | 11.1 us: 1.49x faster                                    |
| sqlglot_transpile        | 1.48 ms                                                     | 1.01 ms: 1.46x faster                                    |
| hexiom                   | 5.74 ms                                                     | 4.04 ms: 1.42x faster                                    |
| pickle_pure_python       | 270 us                                                      | 192 us: 1.40x faster                                     |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.51 sec: 1.40x faster                                   |
| pyflate                  | 409 ms                                                      | 302 ms: 1.36x faster                                     |
| pycparser                | 930 ms                                                      | 687 ms: 1.35x faster                                     |
| scimark_lu               | 85.8 ms                                                     | 63.9 ms: 1.34x faster                                    |
| unpickle_pure_python     | 183 us                                                      | 137 us: 1.34x faster                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.8 ms: 1.31x faster                                    |
| html5lib                 | 51.0 ms                                                     | 39.1 ms: 1.30x faster                                    |
| mako                     | 9.03 ms                                                     | 6.96 ms: 1.30x faster                                    |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                    |
| scimark_sor              | 106 ms                                                      | 83.8 ms: 1.27x faster                                    |
| tornado_http             | 108 ms                                                      | 86.1 ms: 1.26x faster                                    |
| django_template          | 28.9 ms                                                     | 23.0 ms: 1.26x faster                                    |
| genshi_xml               | 41.0 ms                                                     | 32.8 ms: 1.25x faster                                    |
| crypto_pyaes             | 62.5 ms                                                     | 50.1 ms: 1.25x faster                                    |
| regex_compile            | 106 ms                                                      | 85.5 ms: 1.24x faster                                    |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.22x faster                                    |
| thrift                   | 617 us                                                      | 521 us: 1.19x faster                                     |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.16x faster                                    |
| sympy_sum                | 107 ms                                                      | 92.3 ms: 1.16x faster                                    |
| pprint_pformat           | 1.22 sec                                                    | 1.05 sec: 1.16x faster                                   |
| deepcopy_memo            | 28.8 us                                                     | 24.9 us: 1.15x faster                                    |
| chameleon                | 5.79 ms                                                     | 5.03 ms: 1.15x faster                                    |
| tomli_loads              | 1.67 sec                                                    | 1.46 sec: 1.14x faster                                   |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                     |
| 2to3                     | 246 ms                                                      | 215 ms: 1.14x faster                                     |
| pprint_safe_repr         | 592 ms                                                      | 518 ms: 1.14x faster                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 35.0 ms: 1.14x faster                                    |
| bench_thread_pool        | 958 us                                                      | 844 us: 1.13x faster                                     |
| sqlite_synth             | 1.91 us                                                     | 1.69 us: 1.13x faster                                    |
| nqueens                  | 66.6 ms                                                     | 59.4 ms: 1.12x faster                                    |
| xml_etree_process        | 44.5 ms                                                     | 39.7 ms: 1.12x faster                                    |
| sqlglot_normalize        | 205 ms                                                      | 184 ms: 1.11x faster                                     |
| float                    | 61.7 ms                                                     | 55.6 ms: 1.11x faster                                    |
| mdp                      | 1.78 sec                                                    | 1.61 sec: 1.11x faster                                   |
| docutils                 | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                   |
| spectral_norm            | 77.3 ms                                                     | 70.0 ms: 1.10x faster                                    |
| deepcopy                 | 255 us                                                      | 235 us: 1.09x faster                                     |
| sympy_str                | 194 ms                                                      | 179 ms: 1.09x faster                                     |
| logging_format           | 6.76 us                                                     | 6.44 us: 1.05x faster                                    |
| deepcopy_reduce          | 2.20 us                                                     | 2.10 us: 1.05x faster                                    |
| logging_simple           | 6.22 us                                                     | 6.01 us: 1.03x faster                                    |
| regex_v8                 | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                    |
| sympy_expand             | 314 ms                                                      | 307 ms: 1.02x faster                                     |
| meteor_contest           | 75.9 ms                                                     | 74.3 ms: 1.02x faster                                    |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                     |
| nbody                    | 71.3 ms                                                     | 72.4 ms: 1.02x slower                                    |
| json                     | 3.14 ms                                                     | 3.21 ms: 1.02x slower                                    |
| fannkuch                 | 256 ms                                                      | 265 ms: 1.04x slower                                     |
| xml_etree_generate       | 55.5 ms                                                     | 58.2 ms: 1.05x slower                                    |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.05x slower                                    |
| pathlib                  | 75.7 ms                                                     | 79.8 ms: 1.05x slower                                    |
| python_startup           | 20.6 ms                                                     | 21.7 ms: 1.05x slower                                    |
| pickle                   | 6.85 us                                                     | 7.23 us: 1.06x slower                                    |
| unpickle_list            | 2.71 us                                                     | 2.90 us: 1.07x slower                                    |
| xml_etree_parse          | 96.8 ms                                                     | 104 ms: 1.07x slower                                     |
| pickle_dict              | 17.2 us                                                     | 18.7 us: 1.09x slower                                    |
| xml_etree_iterparse      | 65.0 ms                                                     | 70.9 ms: 1.09x slower                                    |
| scimark_fft              | 187 ms                                                      | 212 ms: 1.13x slower                                     |
| bench_mp_pool            | 62.0 ms                                                     | 70.6 ms: 1.14x slower                                    |
| async_generators         | 222 ms                                                      | 253 ms: 1.14x slower                                     |
| pickle_list              | 2.75 us                                                     | 3.14 us: 1.14x slower                                    |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                    |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.14 ms: 1.15x slower                                    |
| coverage                 | 39.0 ms                                                     | 46.9 ms: 1.20x slower                                    |
| telco                    | 3.94 ms                                                     | 5.05 ms: 1.28x slower                                    |
| create_gc_cycles         | 800 us                                                      | 1.08 ms: 1.34x slower                                    |
| gc_traversal             | 1.41 ms                                                     | 2.80 ms: 1.99x slower                                    |
| Geometric mean           | (ref)                                                       | 1.18x faster                                             |

Benchmark hidden because not significant (3): unpickle, regex_effbot, flaskblogging
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240520-3.14.0a0-7466cb2/bm-20240520-pythonperf1-amd64-zooba-cfg-3.14.0a0-7466cb2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown