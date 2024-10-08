# Results vs. 3.10.4

- fork: python
- ref: 363374cf69a7e2292fe3
- machine: windows-amd64
- commit hash: 363374c
- commit date: 2024-08-10
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 240 ms: 1.02x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.85 sec: 1.03x faster                                                     |
| html5lib       | 51.0 ms                                                     | 42.0 ms: 1.22x faster                                                      |
| tornado_http   | 108 ms                                                      | 96.1 ms: 1.13x faster                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 215 ms: 2.02x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 264 ms: 1.99x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 576 ms: 1.92x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.88x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 50.0 ms: 1.43x faster                                                      |
| float          | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.0 ms: 1.18x faster                                                      |
| regex_dna      | 136 ms                                                      | 124 ms: 1.10x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.94 ms: 1.54x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 182 us: 1.48x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 134 us: 1.37x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.27 sec: 1.31x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.0 ms: 1.17x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 52.9 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.2 ms: 1.04x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 94.9 ms: 1.02x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.08 ms: 1.78x faster                                                      |
| django_template | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.5 ms: 1.13x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 38.6 ms: 1.06x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 117 us: 2.88x faster                                                       |
| async_tree_none          | 435 ms                                                      | 215 ms: 2.02x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 264 ms: 1.99x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 576 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.34 ms: 1.79x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.08 ms: 1.78x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 16.3 us: 1.76x faster                                                      |
| scimark_sor              | 106 ms                                                      | 61.5 ms: 1.73x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 56.5 ns: 1.68x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 46.7 ms: 1.65x faster                                                      |
| pyflate                  | 409 ms                                                      | 248 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 394 ms: 1.62x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.61x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.3 ms: 1.57x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 40.0 ms: 1.57x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 55.3 ms: 1.55x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.94 ms: 1.54x faster                                                      |
| generators               | 32.4 ms                                                     | 21.2 ms: 1.53x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.39 sec: 1.52x faster                                                     |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.7 ms: 1.52x faster                                                      |
| richards_super           | 52.2 ms                                                     | 35.2 ms: 1.48x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 182 us: 1.48x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 828 us: 1.47x faster                                                       |
| nbody                    | 71.3 ms                                                     | 50.0 ms: 1.43x faster                                                      |
| raytrace                 | 273 ms                                                      | 194 ms: 1.41x faster                                                       |
| float                    | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                                      |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.06 ms: 1.39x faster                                                      |
| go                       | 139 ms                                                      | 100 ms: 1.38x faster                                                       |
| pylint                   | 350 ms                                                      | 255 ms: 1.37x faster                                                       |
| richards                 | 42.4 ms                                                     | 31.1 ms: 1.37x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 134 us: 1.37x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 550 ms: 1.33x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.27 sec: 1.31x faster                                                     |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.13 ms: 1.28x faster                                                      |
| scimark_fft              | 187 ms                                                      | 149 ms: 1.25x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 975 ms: 1.25x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 475 ms: 1.25x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.44 sec: 1.23x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 42.0 ms: 1.22x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.75 ms: 1.21x faster                                                      |
| thrift                   | 617 us                                                      | 515 us: 1.20x faster                                                       |
| fannkuch                 | 256 ms                                                      | 217 ms: 1.18x faster                                                       |
| regex_compile            | 106 ms                                                      | 90.0 ms: 1.18x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.9 ms: 1.18x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 38.0 ms: 1.17x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 836 us: 1.15x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.5 ms: 1.13x faster                                                      |
| tornado_http             | 108 ms                                                      | 96.1 ms: 1.13x faster                                                      |
| sympy_sum                | 107 ms                                                      | 96.9 ms: 1.10x faster                                                      |
| regex_dna                | 136 ms                                                      | 124 ms: 1.10x faster                                                       |
| pycparser                | 930 ms                                                      | 851 ms: 1.09x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 61.6 ms: 1.08x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 37.0 ms: 1.08x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 191 ms: 1.08x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 38.6 ms: 1.06x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 71.7 ms: 1.06x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 52.9 ms: 1.05x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.2 ms: 1.04x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.48 us: 1.04x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.7 ms: 1.04x faster                                                      |
| sympy_str                | 194 ms                                                      | 188 ms: 1.04x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.01 us: 1.04x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.85 sec: 1.03x faster                                                     |
| 2to3                     | 246 ms                                                      | 240 ms: 1.02x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 94.9 ms: 1.02x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| sympy_expand             | 314 ms                                                      | 330 ms: 1.05x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 81.6 ms: 1.08x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.59 ms: 1.13x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 927 us: 1.16x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.59 ms: 1.16x slower                                                      |
| async_generators         | 222 ms                                                      | 260 ms: 1.17x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 73.4 ms: 1.18x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.18x slower                                                      |
| coverage                 | 39.0 ms                                                     | 46.8 ms: 1.20x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                               |

Benchmark hidden because not significant (2): json, regex_v8
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240810-3.14.0a0-363374c-JIT/bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown