
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 61f1e67
- commit date: 2023-02-18
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| chameleon      | 4.57 ms                                                | 4.45 ms: 1.03x faster                                  |
| docutils       | 1.47 sec                                               | 1.48 sec: 1.00x slower                                 |
| html5lib       | 34.7 ms                                                | 35.5 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 64.1 ms: 1.02x faster                                  |
| float          | 53.0 ms                                                | 52.4 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 72.9 ms: 1.05x faster                                  |
| regex_v8       | 16.2 ms                                                | 15.7 ms: 1.03x faster                                  |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| regex_effbot   | 2.63 ms                                                | 2.60 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.16 ms: 1.25x faster                                  |
| unpickle_pure_python | 159 us                                                 | 142 us: 1.12x faster                                   |
| xml_etree_parse      | 106 ms                                                 | 96.6 ms: 1.10x faster                                  |
| pickle_pure_python   | 199 us                                                 | 193 us: 1.03x faster                                   |
| unpickle_list        | 2.63 us                                                | 2.56 us: 1.03x faster                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| xml_etree_iterparse  | 69.2 ms                                                | 69.8 ms: 1.01x slower                                  |
| xml_etree_process    | 35.2 ms                                                | 35.9 ms: 1.02x slower                                  |
| xml_etree_generate   | 48.8 ms                                                | 50.2 ms: 1.03x slower                                  |
| pickle               | 7.17 us                                                | 7.50 us: 1.05x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (3): pickle_list, unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.5 ms                                                | 11.4 ms: 1.01x faster                                  |
| python_startup_no_site | 9.31 ms                                                | 9.34 ms: 1.00x slower                                  |
| Geometric mean         | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.49 ms                                                | 7.35 ms: 1.16x faster                                  |
| genshi_text     | 15.3 ms                                                | 14.3 ms: 1.07x faster                                  |
| genshi_xml      | 29.8 ms                                                | 28.2 ms: 1.06x faster                                  |
| django_template | 21.0 ms                                                | 21.3 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.07x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230218-darwin-arm64-python-main-3.12.0a5+-61f1e67 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 456 ms: 1.43x faster                                   |
| json_dumps              | 7.72 ms                                                | 6.16 ms: 1.25x faster                                  |
| mako                    | 8.49 ms                                                | 7.35 ms: 1.16x faster                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.81 ms: 1.14x faster                                  |
| generators              | 28.8 ms                                                | 25.5 ms: 1.13x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 142 us: 1.12x faster                                   |
| hexiom                  | 4.73 ms                                                | 4.30 ms: 1.10x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 96.6 ms: 1.10x faster                                  |
| deltablue               | 2.81 ms                                                | 2.56 ms: 1.10x faster                                  |
| richards                | 32.2 ms                                                | 29.9 ms: 1.08x faster                                  |
| genshi_text             | 15.3 ms                                                | 14.3 ms: 1.07x faster                                  |
| chaos                   | 49.5 ms                                                | 46.5 ms: 1.06x faster                                  |
| genshi_xml              | 29.8 ms                                                | 28.2 ms: 1.06x faster                                  |
| pycparser               | 697 ms                                                 | 662 ms: 1.05x faster                                   |
| regex_compile           | 76.7 ms                                                | 72.9 ms: 1.05x faster                                  |
| deepcopy_memo           | 26.3 us                                                | 25.3 us: 1.04x faster                                  |
| scimark_fft             | 199 ms                                                 | 193 ms: 1.03x faster                                   |
| create_gc_cycles        | 726 us                                                 | 704 us: 1.03x faster                                   |
| regex_v8                | 16.2 ms                                                | 15.7 ms: 1.03x faster                                  |
| async_tree_memoization  | 336 ms                                                 | 325 ms: 1.03x faster                                   |
| sympy_str               | 152 ms                                                 | 147 ms: 1.03x faster                                   |
| pickle_pure_python      | 199 us                                                 | 193 us: 1.03x faster                                   |
| sympy_sum               | 86.0 ms                                                | 83.5 ms: 1.03x faster                                  |
| logging_silent          | 68.0 ns                                                | 66.0 ns: 1.03x faster                                  |
| chameleon               | 4.57 ms                                                | 4.45 ms: 1.03x faster                                  |
| unpack_sequence         | 33.6 ns                                                | 32.7 ns: 1.03x faster                                  |
| unpickle_list           | 2.63 us                                                | 2.56 us: 1.03x faster                                  |
| fannkuch                | 261 ms                                                 | 255 ms: 1.02x faster                                   |
| nbody                   | 65.5 ms                                                | 64.1 ms: 1.02x faster                                  |
| bench_thread_pool       | 473 us                                                 | 463 us: 1.02x faster                                   |
| deepcopy                | 224 us                                                 | 220 us: 1.02x faster                                   |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| pathlib                 | 27.8 ms                                                | 27.4 ms: 1.01x faster                                  |
| python_startup          | 11.5 ms                                                | 11.4 ms: 1.01x faster                                  |
| dulwich_log             | 29.9 ms                                                | 29.5 ms: 1.01x faster                                  |
| sympy_integrate         | 11.5 ms                                                | 11.3 ms: 1.01x faster                                  |
| float                   | 53.0 ms                                                | 52.4 ms: 1.01x faster                                  |
| regex_effbot            | 2.63 ms                                                | 2.60 ms: 1.01x faster                                  |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.24 ms: 1.01x faster                                  |
| gc_traversal            | 2.43 ms                                                | 2.42 ms: 1.01x faster                                  |
| mdp                     | 1.54 sec                                               | 1.53 sec: 1.01x faster                                 |
| go                      | 109 ms                                                 | 108 ms: 1.01x faster                                   |
| coroutines              | 17.7 ms                                                | 17.7 ms: 1.00x faster                                  |
| python_startup_no_site  | 9.31 ms                                                | 9.34 ms: 1.00x slower                                  |
| docutils                | 1.47 sec                                               | 1.48 sec: 1.00x slower                                 |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.93 us: 1.01x slower                                  |
| xml_etree_iterparse     | 69.2 ms                                                | 69.8 ms: 1.01x slower                                  |
| scimark_lu              | 72.1 ms                                                | 72.7 ms: 1.01x slower                                  |
| pprint_pformat          | 950 ms                                                 | 959 ms: 1.01x slower                                   |
| async_tree_cpu_io_mixed | 534 ms                                                 | 541 ms: 1.01x slower                                   |
| pprint_safe_repr        | 465 ms                                                 | 470 ms: 1.01x slower                                   |
| django_template         | 21.0 ms                                                | 21.3 ms: 1.01x slower                                  |
| sqlalchemy_declarative  | 62.7 ms                                                | 63.4 ms: 1.01x slower                                  |
| sqlglot_normalize       | 171 ms                                                 | 173 ms: 1.01x slower                                   |
| sqlglot_optimize        | 31.2 ms                                                | 31.8 ms: 1.02x slower                                  |
| xml_etree_process       | 35.2 ms                                                | 35.9 ms: 1.02x slower                                  |
| html5lib                | 34.7 ms                                                | 35.5 ms: 1.02x slower                                  |
| telco                   | 3.39 ms                                                | 3.47 ms: 1.02x slower                                  |
| meteor_contest          | 73.8 ms                                                | 75.8 ms: 1.03x slower                                  |
| xml_etree_generate      | 48.8 ms                                                | 50.2 ms: 1.03x slower                                  |
| logging_format          | 3.78 us                                                | 3.89 us: 1.03x slower                                  |
| logging_simple          | 3.50 us                                                | 3.61 us: 1.03x slower                                  |
| spectral_norm           | 72.8 ms                                                | 75.2 ms: 1.03x slower                                  |
| scimark_sor             | 83.0 ms                                                | 85.9 ms: 1.03x slower                                  |
| crypto_pyaes            | 51.7 ms                                                | 53.5 ms: 1.03x slower                                  |
| coverage                | 58.6 ms                                                | 61.0 ms: 1.04x slower                                  |
| bench_mp_pool           | 43.2 ms                                                | 45.0 ms: 1.04x slower                                  |
| async_tree_io           | 706 ms                                                 | 736 ms: 1.04x slower                                   |
| pyflate                 | 311 ms                                                 | 325 ms: 1.04x slower                                   |
| pickle                  | 7.17 us                                                | 7.50 us: 1.05x slower                                  |
| thrift                  | 433 us                                                 | 458 us: 1.06x slower                                   |
| sqlite_synth            | 1.27 us                                                | 1.36 us: 1.07x slower                                  |
| raytrace                | 207 ms                                                 | 223 ms: 1.07x slower                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.22 ms: 1.09x slower                                  |
| sqlglot_parse           | 957 us                                                 | 1.05 ms: 1.10x slower                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 52.4 ms: 1.13x slower                                  |
| async_generators        | 195 ms                                                 | 263 ms: 1.35x slower                                   |
| dask                    | 226 ms                                                 | 318 ms: 1.41x slower                                   |
| Geometric mean          | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (11): tornado_http, nqueens, async_tree_none, pickle_list, sympy_expand, json, pidigits, unpickle, 2to3, json_loads, mypy2
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, comprehensions, flaskblogging, gunicorn, pylint
