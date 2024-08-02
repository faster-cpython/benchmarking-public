# Results vs. 3.10.4

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: windows-amd64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 237 ms: 1.04x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                      |
| tornado_http   | 108 ms                                                      | 84.3 ms: 1.29x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 212 ms: 2.06x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 256 ms: 2.05x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 544 ms: 2.04x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 383 ms: 1.66x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.95x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 51.4 ms: 1.39x faster                                                      |
| float          | 61.7 ms                                                     | 45.6 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.1 ms: 1.18x faster                                                      |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 20.1 ms: 1.30x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.89 ms: 1.56x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 180 us: 1.49x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.29 sec: 1.30x faster                                                     |
| unpickle_pure_python | 183 us                                                      | 142 us: 1.29x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 39.2 ms: 1.13x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 53.8 ms: 1.03x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.5 ms: 1.09x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.19 ms: 1.74x faster                                                      |
| django_template | 28.9 ms                                                     | 26.9 ms: 1.08x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 44.9 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 118 us: 2.85x faster                                                       |
| async_tree_none          | 435 ms                                                      | 212 ms: 2.06x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 256 ms: 2.05x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 544 ms: 2.04x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 15.8 us: 1.82x faster                                                      |
| deltablue                | 4.19 ms                                                     | 2.37 ms: 1.77x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.19 ms: 1.74x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 45.3 ms: 1.71x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 383 ms: 1.66x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 58.1 ns: 1.63x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.57x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.89 ms: 1.56x faster                                                      |
| pyflate                  | 409 ms                                                      | 264 ms: 1.55x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 482 ms: 1.52x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 41.1 ms: 1.52x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.9 ms: 1.51x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 180 us: 1.49x faster                                                       |
| pylint                   | 350 ms                                                      | 237 ms: 1.48x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 823 us: 1.48x faster                                                       |
| raytrace                 | 273 ms                                                      | 186 ms: 1.47x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.6 ms: 1.45x faster                                                      |
| go                       | 139 ms                                                      | 97.8 ms: 1.42x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.9 ms: 1.42x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.05 ms: 1.40x faster                                                      |
| nbody                    | 71.3 ms                                                     | 51.4 ms: 1.39x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.52 sec: 1.39x faster                                                     |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                       |
| float                    | 61.7 ms                                                     | 45.6 ms: 1.35x faster                                                      |
| generators               | 32.4 ms                                                     | 24.0 ms: 1.35x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.29 sec: 1.30x faster                                                     |
| richards                 | 42.4 ms                                                     | 32.7 ms: 1.30x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 142 us: 1.29x faster                                                       |
| tornado_http             | 108 ms                                                      | 84.3 ms: 1.29x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.14 ms: 1.27x faster                                                      |
| scimark_fft              | 187 ms                                                      | 151 ms: 1.24x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 776 us: 1.23x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.44 sec: 1.23x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.00 sec: 1.22x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 490 ms: 1.21x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.80 ms: 1.20x faster                                                      |
| thrift                   | 617 us                                                      | 518 us: 1.19x faster                                                       |
| regex_compile            | 106 ms                                                      | 90.1 ms: 1.18x faster                                                      |
| fannkuch                 | 256 ms                                                      | 222 ms: 1.15x faster                                                       |
| sympy_sum                | 107 ms                                                      | 93.1 ms: 1.15x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 75.0 ms: 1.14x faster                                                      |
| pycparser                | 930 ms                                                      | 820 ms: 1.13x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.2 ms: 1.13x faster                                                      |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| scimark_sor              | 106 ms                                                      | 94.3 ms: 1.13x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.6 ms: 1.10x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.1 ms: 1.08x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.77 sec: 1.08x faster                                                     |
| sqlglot_optimize         | 39.8 ms                                                     | 37.0 ms: 1.08x faster                                                      |
| django_template          | 28.9 ms                                                     | 26.9 ms: 1.08x faster                                                      |
| sympy_str                | 194 ms                                                      | 182 ms: 1.07x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 62.6 ms: 1.06x faster                                                      |
| json                     | 3.14 ms                                                     | 2.96 ms: 1.06x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.44 us: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.58 ms: 1.05x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.99 us: 1.04x faster                                                      |
| 2to3                     | 246 ms                                                      | 237 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 53.8 ms: 1.03x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 200 ms: 1.03x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 74.1 ms: 1.03x faster                                                      |
| sympy_expand             | 314 ms                                                      | 316 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.5 ms: 1.09x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 44.9 ms: 1.09x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 70.2 ms: 1.13x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 907 us: 1.13x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.52 ms: 1.15x slower                                                      |
| coverage                 | 39.0 ms                                                     | 46.4 ms: 1.19x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                                      |
| async_generators         | 222 ms                                                      | 271 ms: 1.22x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 20.1 ms: 1.30x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (3): pathlib, pidigits, xml_etree_parse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-pythonperf1-amd64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown