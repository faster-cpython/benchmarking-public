
# Results vs. 3.11.0

- fork: python
- ref: v3.12.0b3
- machine: darwin-arm64
- commit hash: f992a60
- commit date: 2023-06-19
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 170 ms: 1.05x slower                                       |
| docutils       | 1.47 sec                                               | 1.52 sec: 1.03x slower                                     |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                       |
| nbody          | 65.6 ms                                                | 68.8 ms: 1.05x slower                                      |
| float          | 53.0 ms                                                | 56.9 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 76.2 ms: 1.01x faster                                      |
| regex_v8       | 16.1 ms                                                | 16.3 ms: 1.01x slower                                      |
| regex_dna      | 152 ms                                                 | 156 ms: 1.03x slower                                       |
| regex_effbot   | 2.63 ms                                                | 2.79 ms: 1.06x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.31 ms: 1.21x faster                                      |
| unpickle_pure_python | 159 us                                                 | 147 us: 1.08x faster                                       |
| pickle_pure_python   | 201 us                                                 | 191 us: 1.05x faster                                       |
| unpickle             | 9.67 us                                                | 9.24 us: 1.05x faster                                      |
| tomli_loads          | 1.47 sec                                               | 1.40 sec: 1.05x faster                                     |
| pickle_list          | 2.81 us                                                | 2.86 us: 1.02x slower                                      |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                       |
| pickle_dict          | 18.0 us                                                | 18.5 us: 1.03x slower                                      |
| pickle               | 7.15 us                                                | 7.43 us: 1.04x slower                                      |
| xml_etree_iterparse  | 70.1 ms                                                | 74.9 ms: 1.07x slower                                      |
| json_loads           | 16.1 us                                                | 17.6 us: 1.09x slower                                      |
| xml_etree_process    | 35.1 ms                                                | 39.1 ms: 1.12x slower                                      |
| xml_etree_generate   | 48.3 ms                                                | 56.5 ms: 1.17x slower                                      |
| unpickle_list        | 2.65 us                                                | 3.23 us: 1.22x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 9.95 ms: 1.02x faster                                      |
| python_startup         | 12.4 ms                                                | 12.2 ms: 1.02x faster                                      |
| Geometric mean         | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.56 ms: 1.13x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 90.9 us: 3.70x faster                                      |
| asyncio_tcp              | 651 ms                                                 | 445 ms: 1.46x faster                                       |
| json_dumps               | 7.63 ms                                                | 6.31 ms: 1.21x faster                                      |
| chaos                    | 49.4 ms                                                | 41.8 ms: 1.18x faster                                      |
| unpack_sequence          | 34.1 ns                                                | 29.3 ns: 1.16x faster                                      |
| deltablue                | 2.81 ms                                                | 2.42 ms: 1.16x faster                                      |
| coverage                 | 58.4 ms                                                | 50.5 ms: 1.16x faster                                      |
| sqlglot_parse            | 959 us                                                 | 830 us: 1.15x faster                                       |
| richards_super           | 39.2 ms                                                | 34.0 ms: 1.15x faster                                      |
| go                       | 109 ms                                                 | 94.2 ms: 1.15x faster                                      |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.25 sec: 1.15x faster                                     |
| mako                     | 8.53 ms                                                | 7.56 ms: 1.13x faster                                      |
| sqlglot_transpile        | 1.12 ms                                                | 1.00 ms: 1.12x faster                                      |
| hexiom                   | 4.72 ms                                                | 4.24 ms: 1.11x faster                                      |
| unpickle_pure_python     | 159 us                                                 | 147 us: 1.08x faster                                       |
| generators               | 28.8 ms                                                | 26.6 ms: 1.08x faster                                      |
| async_tree_memoization   | 336 ms                                                 | 311 ms: 1.08x faster                                       |
| async_tree_none          | 286 ms                                                 | 266 ms: 1.07x faster                                       |
| scimark_monte_carlo      | 46.5 ms                                                | 43.4 ms: 1.07x faster                                      |
| comprehensions           | 16.1 us                                                | 15.1 us: 1.07x faster                                      |
| richards                 | 32.2 ms                                                | 30.3 ms: 1.06x faster                                      |
| async_tree_io            | 704 ms                                                 | 665 ms: 1.06x faster                                       |
| deepcopy_memo            | 26.3 us                                                | 25.0 us: 1.05x faster                                      |
| pickle_pure_python       | 201 us                                                 | 191 us: 1.05x faster                                       |
| unpickle                 | 9.67 us                                                | 9.24 us: 1.05x faster                                      |
| tomli_loads              | 1.47 sec                                               | 1.40 sec: 1.05x faster                                     |
| sqlalchemy_imperative    | 7.20 ms                                                | 6.94 ms: 1.04x faster                                      |
| pycparser                | 698 ms                                                 | 675 ms: 1.03x faster                                       |
| python_startup_no_site   | 10.2 ms                                                | 9.95 ms: 1.02x faster                                      |
| python_startup           | 12.4 ms                                                | 12.2 ms: 1.02x faster                                      |
| mypy2                    | 195 ms                                                 | 191 ms: 1.02x faster                                       |
| create_gc_cycles         | 716 us                                                 | 705 us: 1.01x faster                                       |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 527 ms: 1.01x faster                                       |
| dulwich_log              | 30.3 ms                                                | 30.0 ms: 1.01x faster                                      |
| scimark_lu               | 73.3 ms                                                | 72.6 ms: 1.01x faster                                      |
| regex_compile            | 76.7 ms                                                | 76.2 ms: 1.01x faster                                      |
| gc_traversal             | 2.42 ms                                                | 2.40 ms: 1.01x faster                                      |
| pyflate                  | 310 ms                                                 | 310 ms: 1.00x faster                                       |
| crypto_pyaes             | 51.7 ms                                                | 51.9 ms: 1.00x slower                                      |
| raytrace                 | 207 ms                                                 | 208 ms: 1.00x slower                                       |
| pidigits                 | 281 ms                                                 | 282 ms: 1.00x slower                                       |
| coroutines               | 17.8 ms                                                | 17.9 ms: 1.01x slower                                      |
| scimark_fft              | 200 ms                                                 | 201 ms: 1.01x slower                                       |
| regex_v8                 | 16.1 ms                                                | 16.3 ms: 1.01x slower                                      |
| meteor_contest           | 73.5 ms                                                | 74.5 ms: 1.01x slower                                      |
| nqueens                  | 59.8 ms                                                | 60.7 ms: 1.02x slower                                      |
| fannkuch                 | 261 ms                                                 | 265 ms: 1.02x slower                                       |
| pickle_list              | 2.81 us                                                | 2.86 us: 1.02x slower                                      |
| logging_silent           | 68.1 ns                                                | 69.3 ns: 1.02x slower                                      |
| logging_simple           | 3.55 us                                                | 3.62 us: 1.02x slower                                      |
| bench_thread_pool        | 474 us                                                 | 484 us: 1.02x slower                                       |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.02x slower                                       |
| deepcopy                 | 223 us                                                 | 228 us: 1.02x slower                                       |
| regex_dna                | 152 ms                                                 | 156 ms: 1.03x slower                                       |
| pickle_dict              | 18.0 us                                                | 18.5 us: 1.03x slower                                      |
| spectral_norm            | 72.6 ms                                                | 74.7 ms: 1.03x slower                                      |
| docutils                 | 1.47 sec                                               | 1.52 sec: 1.03x slower                                     |
| logging_format           | 3.78 us                                                | 3.91 us: 1.03x slower                                      |
| scimark_sor              | 82.6 ms                                                | 85.8 ms: 1.04x slower                                      |
| pickle                   | 7.15 us                                                | 7.43 us: 1.04x slower                                      |
| sqlalchemy_declarative   | 62.6 ms                                                | 65.5 ms: 1.05x slower                                      |
| nbody                    | 65.6 ms                                                | 68.8 ms: 1.05x slower                                      |
| 2to3                     | 161 ms                                                 | 170 ms: 1.05x slower                                       |
| bench_mp_pool            | 43.9 ms                                                | 46.4 ms: 1.06x slower                                      |
| mdp                      | 1.55 sec                                               | 1.64 sec: 1.06x slower                                     |
| regex_effbot             | 2.63 ms                                                | 2.79 ms: 1.06x slower                                      |
| xml_etree_iterparse      | 70.1 ms                                                | 74.9 ms: 1.07x slower                                      |
| float                    | 53.0 ms                                                | 56.9 ms: 1.07x slower                                      |
| pprint_pformat           | 954 ms                                                 | 1.03 sec: 1.08x slower                                     |
| pprint_safe_repr         | 466 ms                                                 | 503 ms: 1.08x slower                                       |
| json                     | 2.78 ms                                                | 3.02 ms: 1.09x slower                                      |
| sqlglot_normalize        | 171 ms                                                 | 186 ms: 1.09x slower                                       |
| json_loads               | 16.1 us                                                | 17.6 us: 1.09x slower                                      |
| telco                    | 3.41 ms                                                | 3.73 ms: 1.09x slower                                      |
| deepcopy_reduce          | 1.91 us                                                | 2.10 us: 1.10x slower                                      |
| sqlglot_optimize         | 31.1 ms                                                | 34.3 ms: 1.10x slower                                      |
| xml_etree_process        | 35.1 ms                                                | 39.1 ms: 1.12x slower                                      |
| xml_etree_generate       | 48.3 ms                                                | 56.5 ms: 1.17x slower                                      |
| pathlib                  | 27.2 ms                                                | 33.1 ms: 1.21x slower                                      |
| unpickle_list            | 2.65 us                                                | 3.23 us: 1.22x slower                                      |
| sqlite_synth             | 1.27 us                                                | 1.63 us: 1.28x slower                                      |
| async_generators         | 196 ms                                                 | 309 ms: 1.58x slower                                       |
| Geometric mean           | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (2): tornado_http, scimark_sparse_mat_mult
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230619-3.12.0b3-f992a60/bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60.json: dask
