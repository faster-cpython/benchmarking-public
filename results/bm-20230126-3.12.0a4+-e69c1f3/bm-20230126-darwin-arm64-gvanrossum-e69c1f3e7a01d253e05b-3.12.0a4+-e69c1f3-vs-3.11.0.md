
# Results vs. 3.11.0

- fork: gvanrossum
- ref: e69c1f3e7a01d253e05b
- machine: darwin-arm64
- commit hash: e69c1f3
- commit date: 2023-01-26
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 181 ms: 1.12x slower                                                       |
| docutils       | 1.47 sec                                               | 1.45 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 64.4 ms: 1.02x faster                                                      |
| float          | 53.0 ms                                                | 52.4 ms: 1.01x faster                                                      |
| pidigits       | 281 ms                                                 | 283 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 73.6 ms: 1.04x faster                                                      |
| regex_dna      | 152 ms                                                 | 150 ms: 1.01x faster                                                       |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                                      |
| regex_v8       | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.15 ms: 1.26x faster                                                      |
| xml_etree_parse      | 106 ms                                                 | 94.8 ms: 1.12x faster                                                      |
| unpickle_pure_python | 159 us                                                 | 145 us: 1.09x faster                                                       |
| pickle_pure_python   | 199 us                                                 | 194 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 69.2 ms                                                | 68.3 ms: 1.01x faster                                                      |
| xml_etree_process    | 35.2 ms                                                | 35.4 ms: 1.00x slower                                                      |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                                      |
| xml_etree_generate   | 48.8 ms                                                | 49.3 ms: 1.01x slower                                                      |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                                      |
| pickle_list          | 2.81 us                                                | 2.84 us: 1.01x slower                                                      |
| unpickle             | 9.70 us                                                | 9.87 us: 1.02x slower                                                      |
| unpickle_list        | 2.63 us                                                | 2.71 us: 1.03x slower                                                      |
| pickle               | 7.17 us                                                | 7.55 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.38 ms: 1.26x faster                                                      |
| python_startup         | 11.5 ms                                                | 9.40 ms: 1.23x faster                                                      |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 7.29 ms: 1.16x faster                                                      |
| genshi_text     | 15.3 ms                                                | 14.8 ms: 1.03x faster                                                      |
| genshi_xml      | 29.8 ms                                                | 28.9 ms: 1.03x faster                                                      |
| django_template | 21.0 ms                                                | 21.1 ms: 1.00x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 395 ms: 1.65x faster                                                       |
| pathlib                 | 27.8 ms                                                | 20.8 ms: 1.33x faster                                                      |
| python_startup_no_site  | 9.31 ms                                                | 7.38 ms: 1.26x faster                                                      |
| json_dumps              | 7.72 ms                                                | 6.15 ms: 1.26x faster                                                      |
| python_startup          | 11.5 ms                                                | 9.40 ms: 1.23x faster                                                      |
| mako                    | 8.49 ms                                                | 7.29 ms: 1.16x faster                                                      |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.83 ms: 1.13x faster                                                      |
| xml_etree_parse         | 106 ms                                                 | 94.8 ms: 1.12x faster                                                      |
| unpickle_pure_python    | 159 us                                                 | 145 us: 1.09x faster                                                       |
| deltablue               | 2.81 ms                                                | 2.59 ms: 1.08x faster                                                      |
| bench_thread_pool       | 473 us                                                 | 447 us: 1.06x faster                                                       |
| richards                | 32.2 ms                                                | 30.7 ms: 1.05x faster                                                      |
| sympy_sum               | 86.0 ms                                                | 82.0 ms: 1.05x faster                                                      |
| dulwich_log             | 29.9 ms                                                | 28.5 ms: 1.05x faster                                                      |
| sympy_str               | 152 ms                                                 | 145 ms: 1.05x faster                                                       |
| regex_compile           | 76.7 ms                                                | 73.6 ms: 1.04x faster                                                      |
| scimark_fft             | 199 ms                                                 | 193 ms: 1.03x faster                                                       |
| genshi_text             | 15.3 ms                                                | 14.8 ms: 1.03x faster                                                      |
| nqueens                 | 61.8 ms                                                | 59.7 ms: 1.03x faster                                                      |
| genshi_xml              | 29.8 ms                                                | 28.9 ms: 1.03x faster                                                      |
| logging_silent          | 68.0 ns                                                | 66.0 ns: 1.03x faster                                                      |
| chaos                   | 49.5 ms                                                | 48.1 ms: 1.03x faster                                                      |
| sympy_integrate         | 11.5 ms                                                | 11.2 ms: 1.03x faster                                                      |
| pycparser               | 697 ms                                                 | 680 ms: 1.02x faster                                                       |
| pickle_pure_python      | 199 us                                                 | 194 us: 1.02x faster                                                       |
| create_gc_cycles        | 726 us                                                 | 711 us: 1.02x faster                                                       |
| fannkuch                | 261 ms                                                 | 255 ms: 1.02x faster                                                       |
| coverage                | 58.6 ms                                                | 57.4 ms: 1.02x faster                                                      |
| deepcopy                | 224 us                                                 | 220 us: 1.02x faster                                                       |
| nbody                   | 65.5 ms                                                | 64.4 ms: 1.02x faster                                                      |
| scimark_monte_carlo     | 46.4 ms                                                | 45.7 ms: 1.02x faster                                                      |
| docutils                | 1.47 sec                                               | 1.45 sec: 1.01x faster                                                     |
| mdp                     | 1.54 sec                                               | 1.52 sec: 1.01x faster                                                     |
| xml_etree_iterparse     | 69.2 ms                                                | 68.3 ms: 1.01x faster                                                      |
| regex_dna               | 152 ms                                                 | 150 ms: 1.01x faster                                                       |
| meteor_contest          | 73.8 ms                                                | 73.0 ms: 1.01x faster                                                      |
| float                   | 53.0 ms                                                | 52.4 ms: 1.01x faster                                                      |
| sympy_expand            | 243 ms                                                 | 241 ms: 1.01x faster                                                       |
| pprint_pformat          | 950 ms                                                 | 941 ms: 1.01x faster                                                       |
| regex_effbot            | 2.63 ms                                                | 2.61 ms: 1.01x faster                                                      |
| scimark_lu              | 72.1 ms                                                | 71.5 ms: 1.01x faster                                                      |
| regex_v8                | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                      |
| deepcopy_memo           | 26.3 us                                                | 26.1 us: 1.01x faster                                                      |
| pprint_safe_repr        | 465 ms                                                 | 462 ms: 1.01x faster                                                       |
| hexiom                  | 4.73 ms                                                | 4.71 ms: 1.01x faster                                                      |
| unpack_sequence         | 33.6 ns                                                | 33.6 ns: 1.00x slower                                                      |
| xml_etree_process       | 35.2 ms                                                | 35.4 ms: 1.00x slower                                                      |
| django_template         | 21.0 ms                                                | 21.1 ms: 1.00x slower                                                      |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                                      |
| crypto_pyaes            | 51.7 ms                                                | 52.1 ms: 1.01x slower                                                      |
| pidigits                | 281 ms                                                 | 283 ms: 1.01x slower                                                       |
| xml_etree_generate      | 48.8 ms                                                | 49.3 ms: 1.01x slower                                                      |
| async_tree_none         | 285 ms                                                 | 288 ms: 1.01x slower                                                       |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                                      |
| pickle_list             | 2.81 us                                                | 2.84 us: 1.01x slower                                                      |
| raytrace                | 207 ms                                                 | 210 ms: 1.01x slower                                                       |
| sqlglot_normalize       | 171 ms                                                 | 174 ms: 1.02x slower                                                       |
| unpickle                | 9.70 us                                                | 9.87 us: 1.02x slower                                                      |
| sqlglot_optimize        | 31.2 ms                                                | 31.7 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed | 534 ms                                                 | 544 ms: 1.02x slower                                                       |
| json                    | 2.77 ms                                                | 2.84 ms: 1.02x slower                                                      |
| logging_format          | 3.78 us                                                | 3.87 us: 1.02x slower                                                      |
| thrift                  | 433 us                                                 | 444 us: 1.03x slower                                                       |
| scimark_sor             | 83.0 ms                                                | 85.2 ms: 1.03x slower                                                      |
| logging_simple          | 3.50 us                                                | 3.60 us: 1.03x slower                                                      |
| async_generators        | 195 ms                                                 | 200 ms: 1.03x slower                                                       |
| unpickle_list           | 2.63 us                                                | 2.71 us: 1.03x slower                                                      |
| pyflate                 | 311 ms                                                 | 322 ms: 1.03x slower                                                       |
| async_tree_io           | 706 ms                                                 | 743 ms: 1.05x slower                                                       |
| coroutines              | 17.7 ms                                                | 18.6 ms: 1.05x slower                                                      |
| sqlglot_transpile       | 1.12 ms                                                | 1.18 ms: 1.05x slower                                                      |
| pickle                  | 7.17 us                                                | 7.55 us: 1.05x slower                                                      |
| sqlglot_parse           | 957 us                                                 | 1.01 ms: 1.06x slower                                                      |
| sqlite_synth            | 1.27 us                                                | 1.36 us: 1.07x slower                                                      |
| 2to3                    | 161 ms                                                 | 181 ms: 1.12x slower                                                       |
| generators              | 28.8 ms                                                | 34.4 ms: 1.19x slower                                                      |
| dask                    | 226 ms                                                 | 317 ms: 1.40x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (10): tornado_http, bench_mp_pool, async_tree_memoization, telco, gc_traversal, spectral_norm, chameleon, go, deepcopy_reduce, html5lib
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, comprehensions, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230126-3.12.0a4+-e69c1f3/bm-20230126-darwin-arm64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3.json: mypy
