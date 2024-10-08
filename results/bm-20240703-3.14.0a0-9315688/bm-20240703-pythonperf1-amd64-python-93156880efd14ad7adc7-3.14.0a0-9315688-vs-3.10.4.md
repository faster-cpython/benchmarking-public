# Results vs. 3.10.4

- fork: python
- ref: 93156880efd14ad7adc7
- machine: windows-amd64
- commit hash: 9315688
- commit date: 2024-07-03
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.8 ms: 1.32x faster                                                      |
| tornado_http   | 108 ms                                                      | 91.1 ms: 1.19x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 545 ms: 2.03x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 259 ms: 2.03x faster                                                       |
| async_tree_none         | 435 ms                                                      | 214 ms: 2.03x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 385 ms: 1.66x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.93x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.9 ms: 1.08x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 80.3 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.8 ms: 1.24x faster                                                      |
| regex_dna      | 136 ms                                                      | 124 ms: 1.10x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 17.4 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.09 ms: 1.50x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 150 us: 1.22x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.1 ms: 1.08x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.57 sec: 1.07x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 92.5 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 59.1 ms: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.2 ms: 1.03x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.52 ms: 1.20x faster                                                      |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 37.0 ms: 1.11x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 109 us: 3.10x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 545 ms: 2.03x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 259 ms: 2.03x faster                                                       |
| async_tree_none          | 435 ms                                                      | 214 ms: 2.03x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.17 ms: 1.93x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 385 ms: 1.66x faster                                                       |
| pylint                   | 350 ms                                                      | 213 ms: 1.64x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.4 ms: 1.57x faster                                                      |
| raytrace                 | 273 ms                                                      | 177 ms: 1.54x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 61.8 ns: 1.53x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.09 ms: 1.50x faster                                                      |
| go                       | 139 ms                                                      | 93.5 ms: 1.49x faster                                                      |
| generators               | 32.4 ms                                                     | 22.3 ms: 1.45x faster                                                      |
| richards                 | 42.4 ms                                                     | 29.6 ms: 1.43x faster                                                      |
| chaos                    | 61.7 ms                                                     | 43.6 ms: 1.41x faster                                                      |
| deepcopy                 | 255 us                                                      | 182 us: 1.40x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.40x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 533 ms: 1.37x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.0 us: 1.37x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 891 us: 1.36x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.30 ms: 1.33x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.8 ms: 1.32x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 65.6 ms: 1.31x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.62 sec: 1.31x faster                                                     |
| pyflate                  | 409 ms                                                      | 315 ms: 1.30x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                       |
| scimark_sor              | 106 ms                                                      | 84.4 ms: 1.26x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.43 sec: 1.25x faster                                                     |
| regex_compile            | 106 ms                                                      | 85.8 ms: 1.24x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 150 us: 1.22x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 51.5 ms: 1.21x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.7 ms: 1.21x faster                                                      |
| mako                     | 9.03 ms                                                     | 7.52 ms: 1.20x faster                                                      |
| tornado_http             | 108 ms                                                      | 91.1 ms: 1.19x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.86 us: 1.19x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.4 ms: 1.18x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 16.8 ms: 1.18x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.0 ms: 1.17x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 827 us: 1.16x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                     |
| thrift                   | 617 us                                                      | 540 us: 1.14x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.14x faster                                                      |
| sympy_str                | 194 ms                                                      | 171 ms: 1.13x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 68.2 ms: 1.13x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 35.2 ms: 1.13x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 37.0 ms: 1.11x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                     |
| regex_dna                | 136 ms                                                      | 124 ms: 1.10x faster                                                       |
| pycparser                | 930 ms                                                      | 848 ms: 1.10x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 543 ms: 1.09x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 188 ms: 1.09x faster                                                       |
| float                    | 61.7 ms                                                     | 56.9 ms: 1.08x faster                                                      |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 41.1 ms: 1.08x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.8 ms: 1.08x faster                                                      |
| sympy_expand             | 314 ms                                                      | 293 ms: 1.07x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.57 sec: 1.07x faster                                                     |
| xml_etree_parse          | 96.8 ms                                                     | 92.5 ms: 1.05x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.31 us: 1.01x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 77.0 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.9 ms: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.2 ms: 1.03x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 59.1 ms: 1.06x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 81.2 ms: 1.07x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 67.8 ms: 1.09x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.98 ms: 1.09x slower                                                      |
| async_generators         | 222 ms                                                      | 245 ms: 1.11x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.12x slower                                                      |
| regex_v8                 | 15.4 ms                                                     | 17.4 ms: 1.12x slower                                                      |
| nbody                    | 71.3 ms                                                     | 80.3 ms: 1.13x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                      |
| fannkuch                 | 256 ms                                                      | 291 ms: 1.14x slower                                                       |
| scimark_fft              | 187 ms                                                      | 213 ms: 1.14x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 911 us: 1.14x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.2 ms: 1.24x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.97 ms: 1.26x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                               |

Benchmark hidden because not significant (2): json, logging_format
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240703-3.14.0a0-9315688/bm-20240703-pythonperf1-amd64-python-93156880efd14ad7adc7-3.14.0a0-9315688.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown