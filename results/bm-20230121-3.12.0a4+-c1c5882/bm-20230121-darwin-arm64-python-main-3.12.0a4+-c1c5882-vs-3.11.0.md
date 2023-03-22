
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: c1c5882
- commit date: 2023-01-21
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 183 ms: 1.14x slower                                   |
| chameleon      | 4.57 ms                                                | 4.60 ms: 1.01x slower                                  |
| docutils       | 1.47 sec                                               | 1.44 sec: 1.02x faster                                 |
| tornado_http   | 72.4 ms                                                | 69.1 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 63.5 ms: 1.03x faster                                  |
| float          | 53.0 ms                                                | 51.4 ms: 1.03x faster                                  |
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 73.4 ms: 1.05x faster                                  |
| regex_dna      | 152 ms                                                 | 149 ms: 1.01x faster                                   |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                  |
| regex_v8       | 16.2 ms                                                | 16.2 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.05 ms: 1.28x faster                                  |
| unpickle_pure_python | 159 us                                                 | 144 us: 1.10x faster                                   |
| xml_etree_parse      | 106 ms                                                 | 101 ms: 1.05x faster                                   |
| pickle_pure_python   | 199 us                                                 | 192 us: 1.04x faster                                   |
| xml_etree_process    | 35.2 ms                                                | 35.4 ms: 1.00x slower                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| xml_etree_generate   | 48.8 ms                                                | 49.2 ms: 1.01x slower                                  |
| json_loads           | 16.1 us                                                | 16.2 us: 1.01x slower                                  |
| xml_etree_iterparse  | 69.2 ms                                                | 69.8 ms: 1.01x slower                                  |
| unpickle_list        | 2.63 us                                                | 2.71 us: 1.03x slower                                  |
| pickle               | 7.17 us                                                | 7.52 us: 1.05x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (2): pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.36 ms: 1.26x faster                                  |
| python_startup         | 11.5 ms                                                | 9.37 ms: 1.23x faster                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.49 ms                                                | 8.14 ms: 1.04x faster                                  |
| genshi_xml      | 29.8 ms                                                | 28.7 ms: 1.04x faster                                  |
| genshi_text     | 15.3 ms                                                | 15.5 ms: 1.01x slower                                  |
| django_template | 21.0 ms                                                | 21.8 ms: 1.03x slower                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 434 ms: 1.50x faster                                   |
| pathlib                 | 27.8 ms                                                | 20.8 ms: 1.33x faster                                  |
| json_dumps              | 7.72 ms                                                | 6.05 ms: 1.28x faster                                  |
| python_startup_no_site  | 9.31 ms                                                | 7.36 ms: 1.26x faster                                  |
| python_startup          | 11.5 ms                                                | 9.37 ms: 1.23x faster                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.79 ms: 1.15x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 144 us: 1.10x faster                                   |
| deltablue               | 2.81 ms                                                | 2.61 ms: 1.08x faster                                  |
| bench_thread_pool       | 473 us                                                 | 447 us: 1.06x faster                                   |
| coverage                | 58.6 ms                                                | 55.5 ms: 1.06x faster                                  |
| richards                | 32.2 ms                                                | 30.5 ms: 1.06x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 101 ms: 1.05x faster                                   |
| tornado_http            | 72.4 ms                                                | 69.1 ms: 1.05x faster                                  |
| regex_compile           | 76.7 ms                                                | 73.4 ms: 1.05x faster                                  |
| dulwich_log             | 29.9 ms                                                | 28.6 ms: 1.05x faster                                  |
| mako                    | 8.49 ms                                                | 8.14 ms: 1.04x faster                                  |
| scimark_fft             | 199 ms                                                 | 192 ms: 1.04x faster                                   |
| create_gc_cycles        | 726 us                                                 | 699 us: 1.04x faster                                   |
| genshi_xml              | 29.8 ms                                                | 28.7 ms: 1.04x faster                                  |
| pickle_pure_python      | 199 us                                                 | 192 us: 1.04x faster                                   |
| chaos                   | 49.5 ms                                                | 47.9 ms: 1.03x faster                                  |
| nbody                   | 65.5 ms                                                | 63.5 ms: 1.03x faster                                  |
| float                   | 53.0 ms                                                | 51.4 ms: 1.03x faster                                  |
| nqueens                 | 61.8 ms                                                | 60.0 ms: 1.03x faster                                  |
| pycparser               | 697 ms                                                 | 679 ms: 1.03x faster                                   |
| fannkuch                | 261 ms                                                 | 254 ms: 1.03x faster                                   |
| logging_silent          | 68.0 ns                                                | 66.4 ns: 1.02x faster                                  |
| async_tree_memoization  | 336 ms                                                 | 328 ms: 1.02x faster                                   |
| unpack_sequence         | 33.6 ns                                                | 32.9 ns: 1.02x faster                                  |
| mdp                     | 1.54 sec                                               | 1.51 sec: 1.02x faster                                 |
| docutils                | 1.47 sec                                               | 1.44 sec: 1.02x faster                                 |
| scimark_sor             | 83.0 ms                                                | 81.8 ms: 1.02x faster                                  |
| pprint_pformat          | 950 ms                                                 | 936 ms: 1.01x faster                                   |
| regex_dna               | 152 ms                                                 | 149 ms: 1.01x faster                                   |
| pprint_safe_repr        | 465 ms                                                 | 460 ms: 1.01x faster                                   |
| deepcopy_memo           | 26.3 us                                                | 26.1 us: 1.01x faster                                  |
| sympy_sum               | 86.0 ms                                                | 85.4 ms: 1.01x faster                                  |
| deepcopy                | 224 us                                                 | 222 us: 1.01x faster                                   |
| regex_effbot            | 2.63 ms                                                | 2.61 ms: 1.01x faster                                  |
| sympy_expand            | 243 ms                                                 | 242 ms: 1.01x faster                                   |
| sympy_integrate         | 11.5 ms                                                | 11.4 ms: 1.00x faster                                  |
| go                      | 109 ms                                                 | 108 ms: 1.00x faster                                   |
| regex_v8                | 16.2 ms                                                | 16.2 ms: 1.00x faster                                  |
| scimark_lu              | 72.1 ms                                                | 72.3 ms: 1.00x slower                                  |
| xml_etree_process       | 35.2 ms                                                | 35.4 ms: 1.00x slower                                  |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                   |
| sqlglot_normalize       | 171 ms                                                 | 172 ms: 1.01x slower                                   |
| chameleon               | 4.57 ms                                                | 4.60 ms: 1.01x slower                                  |
| sqlglot_optimize        | 31.2 ms                                                | 31.4 ms: 1.01x slower                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.92 us: 1.01x slower                                  |
| async_tree_cpu_io_mixed | 534 ms                                                 | 538 ms: 1.01x slower                                   |
| xml_etree_generate      | 48.8 ms                                                | 49.2 ms: 1.01x slower                                  |
| json_loads              | 16.1 us                                                | 16.2 us: 1.01x slower                                  |
| xml_etree_iterparse     | 69.2 ms                                                | 69.8 ms: 1.01x slower                                  |
| crypto_pyaes            | 51.7 ms                                                | 52.2 ms: 1.01x slower                                  |
| logging_simple          | 3.50 us                                                | 3.55 us: 1.01x slower                                  |
| async_generators        | 195 ms                                                 | 197 ms: 1.01x slower                                   |
| genshi_text             | 15.3 ms                                                | 15.5 ms: 1.01x slower                                  |
| logging_format          | 3.78 us                                                | 3.84 us: 1.02x slower                                  |
| spectral_norm           | 72.8 ms                                                | 74.0 ms: 1.02x slower                                  |
| thrift                  | 433 us                                                 | 441 us: 1.02x slower                                   |
| json                    | 2.77 ms                                                | 2.83 ms: 1.02x slower                                  |
| telco                   | 3.39 ms                                                | 3.47 ms: 1.02x slower                                  |
| meteor_contest          | 73.8 ms                                                | 75.5 ms: 1.02x slower                                  |
| unpickle_list           | 2.63 us                                                | 2.71 us: 1.03x slower                                  |
| django_template         | 21.0 ms                                                | 21.8 ms: 1.03x slower                                  |
| pyflate                 | 311 ms                                                 | 322 ms: 1.03x slower                                   |
| async_tree_io           | 706 ms                                                 | 732 ms: 1.04x slower                                   |
| scimark_monte_carlo     | 46.4 ms                                                | 48.3 ms: 1.04x slower                                  |
| pickle                  | 7.17 us                                                | 7.52 us: 1.05x slower                                  |
| raytrace                | 207 ms                                                 | 217 ms: 1.05x slower                                   |
| gc_traversal            | 2.43 ms                                                | 2.56 ms: 1.05x slower                                  |
| coroutines              | 17.7 ms                                                | 18.9 ms: 1.07x slower                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.20 ms: 1.07x slower                                  |
| sqlglot_parse           | 957 us                                                 | 1.04 ms: 1.08x slower                                  |
| sqlite_synth            | 1.27 us                                                | 1.38 us: 1.09x slower                                  |
| 2to3                    | 161 ms                                                 | 183 ms: 1.14x slower                                   |
| generators              | 28.8 ms                                                | 34.1 ms: 1.19x slower                                  |
| dask                    | 226 ms                                                 | 320 ms: 1.41x slower                                   |
| Geometric mean          | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (7): bench_mp_pool, sympy_str, hexiom, pickle_list, async_tree_none, unpickle, html5lib
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, comprehensions, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230121-3.12.0a4+-c1c5882/bm-20230121-darwin-arm64-python-main-3.12.0a4+-c1c5882.json: mypy
