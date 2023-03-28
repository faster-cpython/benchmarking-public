
# Results vs. 3.10.4

- fork: python
- ref: 4ae1a0ecaffe4320fe97
- machine: darwin-arm64
- commit hash: 4ae1a0e
- commit date: 2022-10-25
- overall geometric mean: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-darwin-arm64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 165 ms: 1.22x faster                                                  |
| chameleon      | 5.79 ms                                                | 4.58 ms: 1.27x faster                                                 |
| docutils       | 1.78 sec                                               | 1.48 sec: 1.20x faster                                                |
| html5lib       | 44.2 ms                                                | 36.5 ms: 1.21x faster                                                 |
| tornado_http   | 91.5 ms                                                | 70.8 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-darwin-arm64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.7 ms: 1.44x faster                                                 |
| float          | 72.4 ms                                                | 56.4 ms: 1.28x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-darwin-arm64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 76.0 ms: 1.27x faster                                                 |
| regex_v8       | 17.6 ms                                                | 16.2 ms: 1.09x faster                                                 |
| regex_dna      | 162 ms                                                 | 153 ms: 1.05x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.68 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-darwin-arm64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.40 ms                                                | 6.14 ms: 1.37x faster                                                 |
| pickle_pure_python   | 283 us                                                 | 208 us: 1.36x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 34.9 ms: 1.28x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 162 us: 1.26x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 47.2 ms: 1.15x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 93.9 ms: 1.13x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 68.2 ms: 1.06x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.58 us: 1.04x faster                                                 |
| json_loads           | 16.9 us                                                | 16.4 us: 1.03x faster                                                 |
| unpickle             | 9.89 us                                                | 9.71 us: 1.02x faster                                                 |
| pickle_list          | 2.80 us                                                | 2.82 us: 1.01x slower                                                 |
| pickle               | 7.35 us                                                | 7.62 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-darwin-arm64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.1 ms: 1.01x slower                                                 |
| python_startup_no_site | 8.88 ms                                                | 10.0 ms: 1.13x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-darwin-arm64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 8.16 ms: 1.28x faster                                                 |
| django_template | 27.3 ms                                                | 21.9 ms: 1.25x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 29.8 ms: 1.24x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.5 ms: 1.19x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221025-darwin-arm64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.74 ms: 1.88x faster                                                 |
| logging_silent          | 119 ns                                                 | 66.2 ns: 1.80x faster                                                 |
| richards                | 51.4 ms                                                | 33.6 ms: 1.53x faster                                                 |
| scimark_lu              | 109 ms                                                 | 72.2 ms: 1.51x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 51.9 ms: 1.50x faster                                                 |
| async_tree_memoization  | 490 ms                                                 | 331 ms: 1.48x faster                                                  |
| raytrace                | 325 ms                                                 | 222 ms: 1.47x faster                                                  |
| nbody                   | 93.3 ms                                                | 64.7 ms: 1.44x faster                                                 |
| go                      | 165 ms                                                 | 119 ms: 1.39x faster                                                  |
| async_tree_none         | 400 ms                                                 | 292 ms: 1.37x faster                                                  |
| json_dumps              | 8.40 ms                                                | 6.14 ms: 1.37x faster                                                 |
| pickle_pure_python      | 283 us                                                 | 208 us: 1.36x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 748 ms: 1.36x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.01 ms: 1.35x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 54.5 ms: 1.33x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.18 ms: 1.33x faster                                                 |
| chaos                   | 66.7 ms                                                | 50.4 ms: 1.32x faster                                                 |
| thrift                  | 580 us                                                 | 441 us: 1.32x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 72.9 ms: 1.31x faster                                                 |
| pycparser               | 916 ms                                                 | 701 ms: 1.31x faster                                                  |
| tornado_http            | 91.5 ms                                                | 70.8 ms: 1.29x faster                                                 |
| pyflate                 | 453 ms                                                 | 351 ms: 1.29x faster                                                  |
| mako                    | 10.5 ms                                                | 8.16 ms: 1.28x faster                                                 |
| float                   | 72.4 ms                                                | 56.4 ms: 1.28x faster                                                 |
| xml_etree_process       | 44.8 ms                                                | 34.9 ms: 1.28x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.93 ms: 1.28x faster                                                 |
| create_gc_cycles        | 880 us                                                 | 693 us: 1.27x faster                                                  |
| regex_compile           | 96.4 ms                                                | 76.0 ms: 1.27x faster                                                 |
| chameleon               | 5.79 ms                                                | 4.58 ms: 1.27x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.66 us: 1.26x faster                                                 |
| scimark_sor             | 126 ms                                                 | 100 ms: 1.26x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 162 us: 1.26x faster                                                  |
| logging_format          | 4.97 us                                                | 3.96 us: 1.25x faster                                                 |
| pprint_safe_repr        | 606 ms                                                 | 486 ms: 1.25x faster                                                  |
| django_template         | 27.3 ms                                                | 21.9 ms: 1.25x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 29.8 ms: 1.24x faster                                                 |
| pprint_pformat          | 1.23 sec                                               | 992 ms: 1.24x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.78 ms: 1.24x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 30.4 ms: 1.22x faster                                                 |
| 2to3                    | 201 ms                                                 | 165 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 551 ms: 1.21x faster                                                  |
| html5lib                | 44.2 ms                                                | 36.5 ms: 1.21x faster                                                 |
| docutils                | 1.78 sec                                               | 1.48 sec: 1.20x faster                                                |
| genshi_text             | 18.4 ms                                                | 15.5 ms: 1.19x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 29.1 us: 1.18x faster                                                 |
| fannkuch                | 317 ms                                                 | 268 ms: 1.18x faster                                                  |
| sqlglot_optimize        | 38.0 ms                                                | 32.1 ms: 1.18x faster                                                 |
| scimark_fft             | 230 ms                                                 | 197 ms: 1.17x faster                                                  |
| dask                    | 265 ms                                                 | 227 ms: 1.17x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 468 us: 1.17x faster                                                  |
| deepcopy                | 281 us                                                 | 241 us: 1.17x faster                                                  |
| async_generators        | 234 ms                                                 | 201 ms: 1.17x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 2.04 us: 1.17x faster                                                 |
| mypy2                   | 307 ms                                                 | 265 ms: 1.16x faster                                                  |
| xml_etree_generate      | 54.2 ms                                                | 47.2 ms: 1.15x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 11.7 ms: 1.14x faster                                                 |
| pylint                  | 307 ms                                                 | 270 ms: 1.14x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 93.9 ms: 1.13x faster                                                 |
| nqueens                 | 68.2 ms                                                | 60.6 ms: 1.13x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 174 ms: 1.12x faster                                                  |
| unpack_sequence         | 37.4 ns                                                | 33.3 ns: 1.12x faster                                                 |
| generators              | 32.7 ms                                                | 29.2 ms: 1.12x faster                                                 |
| sympy_expand            | 275 ms                                                 | 247 ms: 1.12x faster                                                  |
| sympy_str               | 169 ms                                                 | 153 ms: 1.11x faster                                                  |
| telco                   | 3.63 ms                                                | 3.32 ms: 1.09x faster                                                 |
| json                    | 3.08 ms                                                | 2.82 ms: 1.09x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.52 sec: 1.09x faster                                                |
| regex_v8                | 17.6 ms                                                | 16.2 ms: 1.09x faster                                                 |
| sympy_sum               | 93.6 ms                                                | 86.4 ms: 1.08x faster                                                 |
| coroutines              | 20.2 ms                                                | 19.0 ms: 1.06x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 68.2 ms: 1.06x faster                                                 |
| regex_dna               | 162 ms                                                 | 153 ms: 1.05x faster                                                  |
| comprehensions          | 17.6 us                                                | 16.9 us: 1.04x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.58 us: 1.04x faster                                                 |
| pathlib                 | 28.8 ms                                                | 27.7 ms: 1.04x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.42 us: 1.04x faster                                                 |
| json_loads              | 16.9 us                                                | 16.4 us: 1.03x faster                                                 |
| asyncio_tcp             | 670 ms                                                 | 651 ms: 1.03x faster                                                  |
| unpickle                | 9.89 us                                                | 9.71 us: 1.02x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 76.9 ms: 1.02x faster                                                 |
| pidigits                | 282 ms                                                 | 281 ms: 1.01x faster                                                  |
| pickle_list             | 2.80 us                                                | 2.82 us: 1.01x slower                                                 |
| gc_traversal            | 2.39 ms                                                | 2.42 ms: 1.01x slower                                                 |
| python_startup          | 11.9 ms                                                | 12.1 ms: 1.01x slower                                                 |
| pickle                  | 7.35 us                                                | 7.62 us: 1.04x slower                                                 |
| regex_effbot            | 2.46 ms                                                | 2.68 ms: 1.09x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 43.7 ms: 1.10x slower                                                 |
| python_startup_no_site  | 8.88 ms                                                | 10.0 ms: 1.13x slower                                                 |
| coverage                | 42.0 ms                                                | 53.1 ms: 1.26x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.19x faster                                                          |

Benchmark hidden because not significant (1): pickle_dict
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
