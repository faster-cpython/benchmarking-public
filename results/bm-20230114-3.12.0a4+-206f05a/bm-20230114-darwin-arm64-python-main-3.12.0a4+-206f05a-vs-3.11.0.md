
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 206f05a
- commit date: 2023-01-14
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 183 ms: 1.13x slower                                   |
| docutils       | 1.47 sec                                               | 1.44 sec: 1.02x faster                                 |
| tornado_http   | 72.4 ms                                                | 68.3 ms: 1.06x faster                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (2): chameleon, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 63.4 ms: 1.03x faster                                  |
| float          | 53.0 ms                                                | 51.5 ms: 1.03x faster                                  |
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 74.6 ms: 1.03x faster                                  |
| regex_dna      | 152 ms                                                 | 154 ms: 1.02x slower                                   |
| regex_effbot   | 2.63 ms                                                | 2.73 ms: 1.04x slower                                  |
| regex_v8       | 16.2 ms                                                | 16.8 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.12 ms: 1.26x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 93.1 ms: 1.14x faster                                  |
| unpickle_pure_python | 159 us                                                 | 142 us: 1.12x faster                                   |
| xml_etree_iterparse  | 69.2 ms                                                | 66.4 ms: 1.04x faster                                  |
| pickle_pure_python   | 199 us                                                 | 194 us: 1.02x faster                                   |
| xml_etree_generate   | 48.8 ms                                                | 48.0 ms: 1.02x faster                                  |
| xml_etree_process    | 35.2 ms                                                | 34.8 ms: 1.01x faster                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| unpickle             | 9.70 us                                                | 9.84 us: 1.01x slower                                  |
| unpickle_list        | 2.63 us                                                | 2.71 us: 1.03x slower                                  |
| pickle_list          | 2.81 us                                                | 2.89 us: 1.03x slower                                  |
| pickle               | 7.17 us                                                | 7.56 us: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.34 ms: 1.27x faster                                  |
| python_startup         | 11.5 ms                                                | 9.33 ms: 1.24x faster                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 29.8 ms                                                | 28.4 ms: 1.05x faster                                  |
| mako            | 8.49 ms                                                | 8.10 ms: 1.05x faster                                  |
| django_template | 21.0 ms                                                | 21.7 ms: 1.03x slower                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 408 ms: 1.60x faster                                   |
| pathlib                 | 27.8 ms                                                | 20.9 ms: 1.33x faster                                  |
| python_startup_no_site  | 9.31 ms                                                | 7.34 ms: 1.27x faster                                  |
| json_dumps              | 7.72 ms                                                | 6.12 ms: 1.26x faster                                  |
| python_startup          | 11.5 ms                                                | 9.33 ms: 1.24x faster                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.79 ms: 1.15x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 93.1 ms: 1.14x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 142 us: 1.12x faster                                   |
| deltablue               | 2.81 ms                                                | 2.61 ms: 1.07x faster                                  |
| richards                | 32.2 ms                                                | 30.4 ms: 1.06x faster                                  |
| tornado_http            | 72.4 ms                                                | 68.3 ms: 1.06x faster                                  |
| bench_thread_pool       | 473 us                                                 | 447 us: 1.06x faster                                   |
| create_gc_cycles        | 726 us                                                 | 690 us: 1.05x faster                                   |
| genshi_xml              | 29.8 ms                                                | 28.4 ms: 1.05x faster                                  |
| mako                    | 8.49 ms                                                | 8.10 ms: 1.05x faster                                  |
| dulwich_log             | 29.9 ms                                                | 28.6 ms: 1.05x faster                                  |
| xml_etree_iterparse     | 69.2 ms                                                | 66.4 ms: 1.04x faster                                  |
| coverage                | 58.6 ms                                                | 56.4 ms: 1.04x faster                                  |
| nbody                   | 65.5 ms                                                | 63.4 ms: 1.03x faster                                  |
| float                   | 53.0 ms                                                | 51.5 ms: 1.03x faster                                  |
| regex_compile           | 76.7 ms                                                | 74.6 ms: 1.03x faster                                  |
| mdp                     | 1.54 sec                                               | 1.50 sec: 1.03x faster                                 |
| logging_silent          | 68.0 ns                                                | 66.2 ns: 1.03x faster                                  |
| async_tree_memoization  | 336 ms                                                 | 327 ms: 1.03x faster                                   |
| bench_mp_pool           | 43.2 ms                                                | 42.1 ms: 1.03x faster                                  |
| scimark_fft             | 199 ms                                                 | 195 ms: 1.03x faster                                   |
| unpack_sequence         | 33.6 ns                                                | 32.8 ns: 1.02x faster                                  |
| pickle_pure_python      | 199 us                                                 | 194 us: 1.02x faster                                   |
| fannkuch                | 261 ms                                                 | 255 ms: 1.02x faster                                   |
| pycparser               | 697 ms                                                 | 682 ms: 1.02x faster                                   |
| docutils                | 1.47 sec                                               | 1.44 sec: 1.02x faster                                 |
| xml_etree_generate      | 48.8 ms                                                | 48.0 ms: 1.02x faster                                  |
| deepcopy_memo           | 26.3 us                                                | 25.9 us: 1.02x faster                                  |
| deepcopy                | 224 us                                                 | 220 us: 1.01x faster                                   |
| scimark_sor             | 83.0 ms                                                | 82.0 ms: 1.01x faster                                  |
| xml_etree_process       | 35.2 ms                                                | 34.8 ms: 1.01x faster                                  |
| pprint_pformat          | 950 ms                                                 | 939 ms: 1.01x faster                                   |
| gc_traversal            | 2.43 ms                                                | 2.41 ms: 1.01x faster                                  |
| sympy_expand            | 243 ms                                                 | 241 ms: 1.01x faster                                   |
| deepcopy_reduce         | 1.91 us                                                | 1.90 us: 1.01x faster                                  |
| sympy_integrate         | 11.5 ms                                                | 11.4 ms: 1.01x faster                                  |
| go                      | 109 ms                                                 | 108 ms: 1.01x faster                                   |
| sqlglot_normalize       | 171 ms                                                 | 171 ms: 1.00x slower                                   |
| scimark_lu              | 72.1 ms                                                | 72.3 ms: 1.00x slower                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| logging_format          | 3.78 us                                                | 3.79 us: 1.00x slower                                  |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                   |
| meteor_contest          | 73.8 ms                                                | 74.5 ms: 1.01x slower                                  |
| async_tree_cpu_io_mixed | 534 ms                                                 | 540 ms: 1.01x slower                                   |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| spectral_norm           | 72.8 ms                                                | 73.6 ms: 1.01x slower                                  |
| unpickle                | 9.70 us                                                | 9.84 us: 1.01x slower                                  |
| regex_dna               | 152 ms                                                 | 154 ms: 1.02x slower                                   |
| chaos                   | 49.5 ms                                                | 50.3 ms: 1.02x slower                                  |
| json                    | 2.77 ms                                                | 2.82 ms: 1.02x slower                                  |
| thrift                  | 433 us                                                 | 442 us: 1.02x slower                                   |
| crypto_pyaes            | 51.7 ms                                                | 52.9 ms: 1.02x slower                                  |
| pyflate                 | 311 ms                                                 | 319 ms: 1.03x slower                                   |
| async_generators        | 195 ms                                                 | 200 ms: 1.03x slower                                   |
| unpickle_list           | 2.63 us                                                | 2.71 us: 1.03x slower                                  |
| pickle_list             | 2.81 us                                                | 2.89 us: 1.03x slower                                  |
| django_template         | 21.0 ms                                                | 21.7 ms: 1.03x slower                                  |
| regex_effbot            | 2.63 ms                                                | 2.73 ms: 1.04x slower                                  |
| regex_v8                | 16.2 ms                                                | 16.8 ms: 1.04x slower                                  |
| hexiom                  | 4.73 ms                                                | 4.92 ms: 1.04x slower                                  |
| async_tree_io           | 706 ms                                                 | 737 ms: 1.04x slower                                   |
| coroutines              | 17.7 ms                                                | 18.6 ms: 1.05x slower                                  |
| pickle                  | 7.17 us                                                | 7.56 us: 1.06x slower                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.18 ms: 1.06x slower                                  |
| sqlglot_parse           | 957 us                                                 | 1.02 ms: 1.07x slower                                  |
| raytrace                | 207 ms                                                 | 223 ms: 1.08x slower                                   |
| sqlite_synth            | 1.27 us                                                | 1.38 us: 1.08x slower                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 50.6 ms: 1.09x slower                                  |
| 2to3                    | 161 ms                                                 | 183 ms: 1.13x slower                                   |
| generators              | 28.8 ms                                                | 33.6 ms: 1.17x slower                                  |
| dask                    | 226 ms                                                 | 321 ms: 1.42x slower                                   |
| Geometric mean          | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (11): nqueens, sympy_str, genshi_text, telco, sympy_sum, pprint_safe_repr, async_tree_none, logging_simple, sqlglot_optimize, html5lib, chameleon
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, comprehensions, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230114-3.12.0a4+-206f05a/bm-20230114-darwin-arm64-python-main-3.12.0a4+-206f05a.json: mypy
