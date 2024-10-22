# Results vs. 3.10.4

- fork: python
- ref: 363374cf69a7e2292fe3
- machine: windows-amd64
- commit hash: 363374c
- commit date: 2024-08-10
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 233 ms: 1.06x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.78 sec: 1.08x faster                                                     |
| html5lib       | 51.0 ms                                                     | 42.4 ms: 1.20x faster                                                      |
| tornado_http   | 108 ms                                                      | 94.9 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 220 ms: 1.98x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 266 ms: 1.98x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 588 ms: 1.89x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.86x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.5 ms: 1.11x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 84.9 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| regex_compile  | 106 ms                                                      | 92.3 ms: 1.15x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.34 ms: 1.44x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 215 us: 1.25x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 153 us: 1.20x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.7 ms: 1.07x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 95.4 ms: 1.01x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 59.0 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 69.7 ms: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.85 ms: 1.32x faster                                                      |
| django_template | 28.9 ms                                                     | 24.8 ms: 1.17x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.7 ms: 1.12x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 118 us: 2.85x faster                                                       |
| async_tree_none          | 435 ms                                                      | 220 ms: 1.98x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 266 ms: 1.98x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 588 ms: 1.89x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.29 ms: 1.83x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| pylint                   | 350 ms                                                      | 230 ms: 1.52x faster                                                       |
| generators               | 32.4 ms                                                     | 21.4 ms: 1.52x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 64.7 ns: 1.46x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.34 ms: 1.44x faster                                                      |
| raytrace                 | 273 ms                                                      | 193 ms: 1.41x faster                                                       |
| chaos                    | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 878 us: 1.38x faster                                                       |
| go                       | 139 ms                                                      | 101 ms: 1.38x faster                                                       |
| richards_super           | 52.2 ms                                                     | 37.9 ms: 1.38x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 535 ms: 1.37x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.55 sec: 1.36x faster                                                     |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.36x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 21.1 us: 1.36x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.09 ms: 1.35x faster                                                      |
| deepcopy                 | 255 us                                                      | 191 us: 1.33x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 64.7 ms: 1.33x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.85 ms: 1.32x faster                                                      |
| richards                 | 42.4 ms                                                     | 33.7 ms: 1.26x faster                                                      |
| pyflate                  | 409 ms                                                      | 325 ms: 1.26x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 215 us: 1.25x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.59 ms: 1.25x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.9 ms: 1.20x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 42.4 ms: 1.20x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 153 us: 1.20x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 52.1 ms: 1.20x faster                                                      |
| thrift                   | 617 us                                                      | 524 us: 1.18x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 814 us: 1.18x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.2 ms: 1.17x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.53 sec: 1.17x faster                                                     |
| django_template          | 28.9 ms                                                     | 24.8 ms: 1.17x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.8 ms: 1.15x faster                                                      |
| regex_compile            | 106 ms                                                      | 92.3 ms: 1.15x faster                                                      |
| tornado_http             | 108 ms                                                      | 94.9 ms: 1.14x faster                                                      |
| scimark_sor              | 106 ms                                                      | 93.1 ms: 1.14x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.12x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.96 us: 1.12x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.7 ms: 1.12x faster                                                      |
| float                    | 61.7 ms                                                     | 55.5 ms: 1.11x faster                                                      |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.6 ms: 1.09x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.78 sec: 1.08x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 41.7 ms: 1.07x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 73.0 ms: 1.06x faster                                                      |
| 2to3                     | 246 ms                                                      | 233 ms: 1.06x faster                                                       |
| sympy_expand             | 314 ms                                                      | 299 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 198 ms: 1.04x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.18 sec: 1.03x faster                                                     |
| tomli_loads              | 1.67 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 575 ms: 1.03x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 65.1 ms: 1.02x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 95.4 ms: 1.01x faster                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.88 us: 1.02x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 77.4 ms: 1.02x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.37 us: 1.02x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.81 ms: 1.03x slower                                                      |
| json                     | 3.14 ms                                                     | 3.32 ms: 1.06x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.9 ms: 1.06x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 59.0 ms: 1.06x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 69.7 ms: 1.07x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 81.2 ms: 1.07x slower                                                      |
| scimark_fft              | 187 ms                                                      | 203 ms: 1.08x slower                                                       |
| async_generators         | 222 ms                                                      | 246 ms: 1.11x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.11x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 69.5 ms: 1.12x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 920 us: 1.15x slower                                                       |
| fannkuch                 | 256 ms                                                      | 297 ms: 1.16x slower                                                       |
| nbody                    | 71.3 ms                                                     | 84.9 ms: 1.19x slower                                                      |
| coverage                 | 39.0 ms                                                     | 47.3 ms: 1.21x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.99 ms: 1.27x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (2): pycparser, regex_v8
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240810-3.14.0a0-363374c/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown