
# Results vs. 3.11.0

- fork: python
- ref: 9f2c479eaf7d922746ef
- machine: darwin-arm64
- commit hash: 9f2c479
- commit date: 2023-01-26
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 185 ms: 1.15x slower                                                   |
| chameleon      | 4.57 ms                                                | 4.52 ms: 1.01x faster                                                  |
| docutils       | 1.47 sec                                               | 1.45 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 51.8 ms: 1.02x faster                                                  |
| nbody          | 65.5 ms                                                | 64.5 ms: 1.02x faster                                                  |
| pidigits       | 281 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 73.7 ms: 1.04x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                  |
| regex_v8       | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                  |
| regex_dna      | 152 ms                                                 | 153 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.23 ms: 1.24x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 93.7 ms: 1.13x faster                                                  |
| unpickle_pure_python | 159 us                                                 | 147 us: 1.08x faster                                                   |
| pickle_pure_python   | 199 us                                                 | 194 us: 1.03x faster                                                   |
| xml_etree_iterparse  | 69.2 ms                                                | 67.7 ms: 1.02x faster                                                  |
| pickle_dict          | 17.9 us                                                | 17.9 us: 1.00x slower                                                  |
| pickle_list          | 2.81 us                                                | 2.83 us: 1.01x slower                                                  |
| xml_etree_generate   | 48.8 ms                                                | 49.3 ms: 1.01x slower                                                  |
| json_loads           | 16.1 us                                                | 16.2 us: 1.01x slower                                                  |
| xml_etree_process    | 35.2 ms                                                | 35.6 ms: 1.01x slower                                                  |
| unpickle             | 9.70 us                                                | 9.89 us: 1.02x slower                                                  |
| unpickle_list        | 2.63 us                                                | 2.77 us: 1.05x slower                                                  |
| pickle               | 7.17 us                                                | 7.56 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.39 ms: 1.26x faster                                                  |
| python_startup         | 11.5 ms                                                | 9.40 ms: 1.23x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 7.27 ms: 1.17x faster                                                  |
| genshi_text     | 15.3 ms                                                | 14.7 ms: 1.04x faster                                                  |
| genshi_xml      | 29.8 ms                                                | 28.9 ms: 1.03x faster                                                  |
| django_template | 21.0 ms                                                | 21.3 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 446 ms: 1.46x faster                                                   |
| pathlib                 | 27.8 ms                                                | 20.7 ms: 1.34x faster                                                  |
| python_startup_no_site  | 9.31 ms                                                | 7.39 ms: 1.26x faster                                                  |
| json_dumps              | 7.72 ms                                                | 6.23 ms: 1.24x faster                                                  |
| python_startup          | 11.5 ms                                                | 9.40 ms: 1.23x faster                                                  |
| mako                    | 8.49 ms                                                | 7.27 ms: 1.17x faster                                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.82 ms: 1.14x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 93.7 ms: 1.13x faster                                                  |
| deltablue               | 2.81 ms                                                | 2.50 ms: 1.12x faster                                                  |
| unpickle_pure_python    | 159 us                                                 | 147 us: 1.08x faster                                                   |
| scimark_sor             | 83.0 ms                                                | 78.3 ms: 1.06x faster                                                  |
| sympy_sum               | 86.0 ms                                                | 81.4 ms: 1.06x faster                                                  |
| bench_thread_pool       | 473 us                                                 | 450 us: 1.05x faster                                                   |
| create_gc_cycles        | 726 us                                                 | 692 us: 1.05x faster                                                   |
| sympy_str               | 152 ms                                                 | 145 ms: 1.05x faster                                                   |
| dulwich_log             | 29.9 ms                                                | 28.5 ms: 1.05x faster                                                  |
| genshi_text             | 15.3 ms                                                | 14.7 ms: 1.04x faster                                                  |
| regex_compile           | 76.7 ms                                                | 73.7 ms: 1.04x faster                                                  |
| richards                | 32.2 ms                                                | 31.1 ms: 1.04x faster                                                  |
| chaos                   | 49.5 ms                                                | 47.8 ms: 1.04x faster                                                  |
| async_tree_memoization  | 336 ms                                                 | 324 ms: 1.04x faster                                                   |
| nqueens                 | 61.8 ms                                                | 59.7 ms: 1.03x faster                                                  |
| scimark_fft             | 199 ms                                                 | 193 ms: 1.03x faster                                                   |
| genshi_xml              | 29.8 ms                                                | 28.9 ms: 1.03x faster                                                  |
| sympy_integrate         | 11.5 ms                                                | 11.1 ms: 1.03x faster                                                  |
| coverage                | 58.6 ms                                                | 56.9 ms: 1.03x faster                                                  |
| pickle_pure_python      | 199 us                                                 | 194 us: 1.03x faster                                                   |
| unpack_sequence         | 33.6 ns                                                | 32.7 ns: 1.03x faster                                                  |
| logging_silent          | 68.0 ns                                                | 66.3 ns: 1.03x faster                                                  |
| pycparser               | 697 ms                                                 | 680 ms: 1.02x faster                                                   |
| deepcopy                | 224 us                                                 | 219 us: 1.02x faster                                                   |
| float                   | 53.0 ms                                                | 51.8 ms: 1.02x faster                                                  |
| xml_etree_iterparse     | 69.2 ms                                                | 67.7 ms: 1.02x faster                                                  |
| fannkuch                | 261 ms                                                 | 256 ms: 1.02x faster                                                   |
| mdp                     | 1.54 sec                                               | 1.51 sec: 1.02x faster                                                 |
| docutils                | 1.47 sec                                               | 1.45 sec: 1.02x faster                                                 |
| scimark_lu              | 72.1 ms                                                | 71.0 ms: 1.02x faster                                                  |
| nbody                   | 65.5 ms                                                | 64.5 ms: 1.02x faster                                                  |
| sympy_expand            | 243 ms                                                 | 240 ms: 1.01x faster                                                   |
| chameleon               | 4.57 ms                                                | 4.52 ms: 1.01x faster                                                  |
| deepcopy_memo           | 26.3 us                                                | 26.0 us: 1.01x faster                                                  |
| regex_effbot            | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                  |
| gc_traversal            | 2.43 ms                                                | 2.41 ms: 1.01x faster                                                  |
| spectral_norm           | 72.8 ms                                                | 72.3 ms: 1.01x faster                                                  |
| regex_v8                | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                  |
| pprint_pformat          | 950 ms                                                 | 946 ms: 1.00x faster                                                   |
| meteor_contest          | 73.8 ms                                                | 73.8 ms: 1.00x faster                                                  |
| pickle_dict             | 17.9 us                                                | 17.9 us: 1.00x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 51.9 ms: 1.00x slower                                                  |
| sqlglot_normalize       | 171 ms                                                 | 172 ms: 1.01x slower                                                   |
| logging_simple          | 3.50 us                                                | 3.53 us: 1.01x slower                                                  |
| sqlglot_optimize        | 31.2 ms                                                | 31.4 ms: 1.01x slower                                                  |
| pidigits                | 281 ms                                                 | 283 ms: 1.01x slower                                                   |
| logging_format          | 3.78 us                                                | 3.80 us: 1.01x slower                                                  |
| pickle_list             | 2.81 us                                                | 2.83 us: 1.01x slower                                                  |
| regex_dna               | 152 ms                                                 | 153 ms: 1.01x slower                                                   |
| xml_etree_generate      | 48.8 ms                                                | 49.3 ms: 1.01x slower                                                  |
| async_tree_none         | 285 ms                                                 | 288 ms: 1.01x slower                                                   |
| json_loads              | 16.1 us                                                | 16.2 us: 1.01x slower                                                  |
| xml_etree_process       | 35.2 ms                                                | 35.6 ms: 1.01x slower                                                  |
| django_template         | 21.0 ms                                                | 21.3 ms: 1.01x slower                                                  |
| go                      | 109 ms                                                 | 110 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed | 534 ms                                                 | 544 ms: 1.02x slower                                                   |
| unpickle                | 9.70 us                                                | 9.89 us: 1.02x slower                                                  |
| thrift                  | 433 us                                                 | 443 us: 1.02x slower                                                   |
| async_generators        | 195 ms                                                 | 199 ms: 1.02x slower                                                   |
| json                    | 2.77 ms                                                | 2.84 ms: 1.03x slower                                                  |
| pyflate                 | 311 ms                                                 | 324 ms: 1.04x slower                                                   |
| raytrace                | 207 ms                                                 | 216 ms: 1.04x slower                                                   |
| async_tree_io           | 706 ms                                                 | 742 ms: 1.05x slower                                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.18 ms: 1.05x slower                                                  |
| unpickle_list           | 2.63 us                                                | 2.77 us: 1.05x slower                                                  |
| pickle                  | 7.17 us                                                | 7.56 us: 1.06x slower                                                  |
| sqlglot_parse           | 957 us                                                 | 1.01 ms: 1.06x slower                                                  |
| coroutines              | 17.7 ms                                                | 18.8 ms: 1.06x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.36 us: 1.06x slower                                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 50.4 ms: 1.08x slower                                                  |
| 2to3                    | 161 ms                                                 | 185 ms: 1.15x slower                                                   |
| generators              | 28.8 ms                                                | 34.6 ms: 1.20x slower                                                  |
| dask                    | 226 ms                                                 | 318 ms: 1.41x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (7): tornado_http, telco, hexiom, pprint_safe_repr, deepcopy_reduce, bench_mp_pool, html5lib
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, comprehensions, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230126-3.12.0a4+-9f2c479/bm-20230126-darwin-arm64-python-9f2c479eaf7d922746ef-3.12.0a4+-9f2c479.json: mypy
