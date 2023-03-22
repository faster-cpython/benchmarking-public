
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 5a2b984
- commit date: 2023-02-04
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 182 ms: 1.13x slower                                   |
| chameleon      | 4.57 ms                                                | 4.71 ms: 1.03x slower                                  |
| docutils       | 1.47 sec                                               | 1.45 sec: 1.01x faster                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 64.0 ms: 1.02x faster                                  |
| float          | 53.0 ms                                                | 51.9 ms: 1.02x faster                                  |
| pidigits       | 281 ms                                                 | 283 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 72.1 ms: 1.06x faster                                  |
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                   |
| regex_effbot   | 2.63 ms                                                | 2.63 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.10 ms: 1.27x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 93.9 ms: 1.13x faster                                  |
| pickle_pure_python   | 199 us                                                 | 192 us: 1.03x faster                                   |
| xml_etree_process    | 35.2 ms                                                | 34.4 ms: 1.02x faster                                  |
| xml_etree_generate   | 48.8 ms                                                | 47.8 ms: 1.02x faster                                  |
| xml_etree_iterparse  | 69.2 ms                                                | 67.8 ms: 1.02x faster                                  |
| unpickle_pure_python | 159 us                                                 | 157 us: 1.01x faster                                   |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| unpickle             | 9.70 us                                                | 9.91 us: 1.02x slower                                  |
| unpickle_list        | 2.63 us                                                | 2.71 us: 1.03x slower                                  |
| pickle               | 7.17 us                                                | 7.57 us: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.35 ms: 1.27x faster                                  |
| python_startup         | 11.5 ms                                                | 9.36 ms: 1.23x faster                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.49 ms                                                | 7.16 ms: 1.19x faster                                  |
| genshi_text     | 15.3 ms                                                | 14.3 ms: 1.07x faster                                  |
| genshi_xml      | 29.8 ms                                                | 28.4 ms: 1.05x faster                                  |
| django_template | 21.0 ms                                                | 20.9 ms: 1.00x faster                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 423 ms: 1.54x faster                                   |
| pathlib                 | 27.8 ms                                                | 20.8 ms: 1.34x faster                                  |
| python_startup_no_site  | 9.31 ms                                                | 7.35 ms: 1.27x faster                                  |
| json_dumps              | 7.72 ms                                                | 6.10 ms: 1.27x faster                                  |
| python_startup          | 11.5 ms                                                | 9.36 ms: 1.23x faster                                  |
| mako                    | 8.49 ms                                                | 7.16 ms: 1.19x faster                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.81 ms: 1.14x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 93.9 ms: 1.13x faster                                  |
| hexiom                  | 4.73 ms                                                | 4.32 ms: 1.10x faster                                  |
| deltablue               | 2.81 ms                                                | 2.57 ms: 1.09x faster                                  |
| chaos                   | 49.5 ms                                                | 45.5 ms: 1.09x faster                                  |
| richards                | 32.2 ms                                                | 29.7 ms: 1.08x faster                                  |
| genshi_text             | 15.3 ms                                                | 14.3 ms: 1.07x faster                                  |
| regex_compile           | 76.7 ms                                                | 72.1 ms: 1.06x faster                                  |
| bench_thread_pool       | 473 us                                                 | 447 us: 1.06x faster                                   |
| sympy_sum               | 86.0 ms                                                | 81.9 ms: 1.05x faster                                  |
| genshi_xml              | 29.8 ms                                                | 28.4 ms: 1.05x faster                                  |
| create_gc_cycles        | 726 us                                                 | 696 us: 1.04x faster                                   |
| dulwich_log             | 29.9 ms                                                | 28.6 ms: 1.04x faster                                  |
| sympy_str               | 152 ms                                                 | 145 ms: 1.04x faster                                   |
| async_tree_memoization  | 336 ms                                                 | 322 ms: 1.04x faster                                   |
| pycparser               | 697 ms                                                 | 669 ms: 1.04x faster                                   |
| scimark_fft             | 199 ms                                                 | 192 ms: 1.04x faster                                   |
| logging_silent          | 68.0 ns                                                | 65.7 ns: 1.03x faster                                  |
| pickle_pure_python      | 199 us                                                 | 192 us: 1.03x faster                                   |
| coverage                | 58.6 ms                                                | 57.1 ms: 1.03x faster                                  |
| sympy_integrate         | 11.5 ms                                                | 11.2 ms: 1.02x faster                                  |
| unpack_sequence         | 33.6 ns                                                | 32.8 ns: 1.02x faster                                  |
| xml_etree_process       | 35.2 ms                                                | 34.4 ms: 1.02x faster                                  |
| nbody                   | 65.5 ms                                                | 64.0 ms: 1.02x faster                                  |
| xml_etree_generate      | 48.8 ms                                                | 47.8 ms: 1.02x faster                                  |
| float                   | 53.0 ms                                                | 51.9 ms: 1.02x faster                                  |
| xml_etree_iterparse     | 69.2 ms                                                | 67.8 ms: 1.02x faster                                  |
| fannkuch                | 261 ms                                                 | 256 ms: 1.02x faster                                   |
| scimark_lu              | 72.1 ms                                                | 70.8 ms: 1.02x faster                                  |
| deepcopy                | 224 us                                                 | 220 us: 1.02x faster                                   |
| async_tree_none         | 285 ms                                                 | 280 ms: 1.02x faster                                   |
| deepcopy_memo           | 26.3 us                                                | 25.9 us: 1.02x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 157 us: 1.01x faster                                   |
| regex_dna               | 152 ms                                                 | 150 ms: 1.01x faster                                   |
| mdp                     | 1.54 sec                                               | 1.52 sec: 1.01x faster                                 |
| docutils                | 1.47 sec                                               | 1.45 sec: 1.01x faster                                 |
| gc_traversal            | 2.43 ms                                                | 2.41 ms: 1.01x faster                                  |
| django_template         | 21.0 ms                                                | 20.9 ms: 1.00x faster                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.90 us: 1.00x faster                                  |
| sympy_expand            | 243 ms                                                 | 243 ms: 1.00x faster                                   |
| regex_effbot            | 2.63 ms                                                | 2.63 ms: 1.00x faster                                  |
| pprint_pformat          | 950 ms                                                 | 955 ms: 1.01x slower                                   |
| sqlglot_optimize        | 31.2 ms                                                | 31.4 ms: 1.01x slower                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| pidigits                | 281 ms                                                 | 283 ms: 1.01x slower                                   |
| telco                   | 3.39 ms                                                | 3.43 ms: 1.01x slower                                  |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| pprint_safe_repr        | 465 ms                                                 | 470 ms: 1.01x slower                                   |
| thrift                  | 433 us                                                 | 442 us: 1.02x slower                                   |
| crypto_pyaes            | 51.7 ms                                                | 52.7 ms: 1.02x slower                                  |
| unpickle                | 9.70 us                                                | 9.91 us: 1.02x slower                                  |
| json                    | 2.77 ms                                                | 2.83 ms: 1.02x slower                                  |
| async_generators        | 195 ms                                                 | 200 ms: 1.02x slower                                   |
| scimark_sor             | 83.0 ms                                                | 85.3 ms: 1.03x slower                                  |
| meteor_contest          | 73.8 ms                                                | 75.9 ms: 1.03x slower                                  |
| chameleon               | 4.57 ms                                                | 4.71 ms: 1.03x slower                                  |
| unpickle_list           | 2.63 us                                                | 2.71 us: 1.03x slower                                  |
| async_tree_io           | 706 ms                                                 | 732 ms: 1.04x slower                                   |
| logging_simple          | 3.50 us                                                | 3.64 us: 1.04x slower                                  |
| logging_format          | 3.78 us                                                | 3.93 us: 1.04x slower                                  |
| pickle                  | 7.17 us                                                | 7.57 us: 1.06x slower                                  |
| coroutines              | 17.7 ms                                                | 18.8 ms: 1.06x slower                                  |
| raytrace                | 207 ms                                                 | 219 ms: 1.06x slower                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.19 ms: 1.06x slower                                  |
| sqlglot_parse           | 957 us                                                 | 1.02 ms: 1.07x slower                                  |
| pyflate                 | 311 ms                                                 | 333 ms: 1.07x slower                                   |
| scimark_monte_carlo     | 46.4 ms                                                | 49.8 ms: 1.07x slower                                  |
| sqlite_synth            | 1.27 us                                                | 1.40 us: 1.10x slower                                  |
| 2to3                    | 161 ms                                                 | 182 ms: 1.13x slower                                   |
| generators              | 28.8 ms                                                | 34.1 ms: 1.18x slower                                  |
| dask                    | 226 ms                                                 | 319 ms: 1.41x slower                                   |
| Geometric mean          | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (10): tornado_http, nqueens, bench_mp_pool, spectral_norm, regex_v8, go, sqlglot_normalize, pickle_list, async_tree_cpu_io_mixed, html5lib
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, comprehensions, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230204-3.12.0a4+-5a2b984/bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984.json: mypy
