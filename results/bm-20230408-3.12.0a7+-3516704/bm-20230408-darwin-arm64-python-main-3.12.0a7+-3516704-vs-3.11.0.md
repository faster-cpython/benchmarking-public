
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 3516704
- commit date: 2023-04-08
- overall geometric mean: 1.00x slower \*
- HPT reliability: 98.69%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-darwin-arm64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 168 ms: 1.04x slower                                   |
| chameleon      | 4.60 ms                                                | 4.50 ms: 1.02x faster                                  |
| docutils       | 1.47 sec                                               | 1.50 sec: 1.02x slower                                 |
| html5lib       | 34.7 ms                                                | 36.6 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-darwin-arm64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 60.4 ms: 1.09x faster                                  |
| pidigits       | 281 ms                                                 | 280 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-darwin-arm64-python-main-3.12.0a7+-3516704 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 16.1 ms                                                | 16.1 ms: 1.00x faster                                  |
| regex_dna      | 152 ms                                                 | 152 ms: 1.00x faster                                   |
| regex_effbot   | 2.63 ms                                                | 2.67 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-darwin-arm64-python-main-3.12.0a7+-3516704 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.27 ms: 1.22x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 98.0 ms: 1.10x faster                                  |
| unpickle_pure_python | 159 us                                                 | 149 us: 1.07x faster                                   |
| unpickle             | 9.67 us                                                | 9.11 us: 1.06x faster                                  |
| pickle_pure_python   | 201 us                                                 | 194 us: 1.03x faster                                   |
| unpickle_list        | 2.65 us                                                | 2.66 us: 1.00x slower                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 71.2 ms: 1.01x slower                                  |
| json_loads           | 16.1 us                                                | 16.4 us: 1.02x slower                                  |
| pickle_list          | 2.81 us                                                | 2.87 us: 1.02x slower                                  |
| pickle_dict          | 18.0 us                                                | 18.4 us: 1.02x slower                                  |
| xml_etree_process    | 35.1 ms                                                | 36.8 ms: 1.05x slower                                  |
| pickle               | 7.15 us                                                | 7.52 us: 1.05x slower                                  |
| xml_etree_generate   | 48.3 ms                                                | 51.5 ms: 1.07x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-darwin-arm64-python-main-3.12.0a7+-3516704 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 11.2 ms: 1.11x faster                                  |
| python_startup_no_site | 10.2 ms                                                | 9.23 ms: 1.10x faster                                  |
| Geometric mean         | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-darwin-arm64-python-main-3.12.0a7+-3516704 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.39 ms: 1.15x faster                                  |
| genshi_text     | 15.3 ms                                                | 14.7 ms: 1.04x faster                                  |
| genshi_xml      | 29.8 ms                                                | 29.5 ms: 1.01x faster                                  |
| django_template | 21.0 ms                                                | 21.7 ms: 1.03x slower                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-darwin-arm64-python-main-3.12.0a7+-3516704 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 451 ms: 1.44x faster                                   |
| json_dumps              | 7.63 ms                                                | 6.27 ms: 1.22x faster                                  |
| mako                    | 8.53 ms                                                | 7.39 ms: 1.15x faster                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.82 ms: 1.13x faster                                  |
| python_startup          | 12.4 ms                                                | 11.2 ms: 1.11x faster                                  |
| xml_etree_parse         | 108 ms                                                 | 98.0 ms: 1.10x faster                                  |
| python_startup_no_site  | 10.2 ms                                                | 9.23 ms: 1.10x faster                                  |
| nbody                   | 65.6 ms                                                | 60.4 ms: 1.09x faster                                  |
| deltablue               | 2.81 ms                                                | 2.60 ms: 1.08x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 149 us: 1.07x faster                                   |
| unpickle                | 9.67 us                                                | 9.11 us: 1.06x faster                                  |
| hexiom                  | 4.72 ms                                                | 4.46 ms: 1.06x faster                                  |
| sqlglot_parse           | 959 us                                                 | 906 us: 1.06x faster                                   |
| scimark_fft             | 200 ms                                                 | 189 ms: 1.06x faster                                   |
| chaos                   | 49.4 ms                                                | 47.3 ms: 1.04x faster                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.08 ms: 1.04x faster                                  |
| genshi_text             | 15.3 ms                                                | 14.7 ms: 1.04x faster                                  |
| unpack_sequence         | 34.1 ns                                                | 32.9 ns: 1.04x faster                                  |
| pickle_pure_python      | 201 us                                                 | 194 us: 1.03x faster                                   |
| create_gc_cycles        | 716 us                                                 | 696 us: 1.03x faster                                   |
| richards                | 32.2 ms                                                | 31.4 ms: 1.03x faster                                  |
| scimark_lu              | 73.3 ms                                                | 71.5 ms: 1.02x faster                                  |
| pycparser               | 698 ms                                                 | 682 ms: 1.02x faster                                   |
| chameleon               | 4.60 ms                                                | 4.50 ms: 1.02x faster                                  |
| generators              | 28.8 ms                                                | 28.2 ms: 1.02x faster                                  |
| deepcopy_memo           | 26.3 us                                                | 25.9 us: 1.02x faster                                  |
| genshi_xml              | 29.8 ms                                                | 29.5 ms: 1.01x faster                                  |
| logging_silent          | 68.1 ns                                                | 67.3 ns: 1.01x faster                                  |
| dulwich_log             | 30.3 ms                                                | 30.1 ms: 1.01x faster                                  |
| bench_thread_pool       | 474 us                                                 | 472 us: 1.01x faster                                   |
| mdp                     | 1.55 sec                                               | 1.54 sec: 1.01x faster                                 |
| meteor_contest          | 73.5 ms                                                | 73.2 ms: 1.00x faster                                  |
| regex_v8                | 16.1 ms                                                | 16.1 ms: 1.00x faster                                  |
| pidigits                | 281 ms                                                 | 280 ms: 1.00x faster                                   |
| regex_dna               | 152 ms                                                 | 152 ms: 1.00x faster                                   |
| unpickle_list           | 2.65 us                                                | 2.66 us: 1.00x slower                                  |
| gc_traversal            | 2.42 ms                                                | 2.42 ms: 1.00x slower                                  |
| json                    | 2.78 ms                                                | 2.80 ms: 1.01x slower                                  |
| spectral_norm           | 72.6 ms                                                | 73.1 ms: 1.01x slower                                  |
| telco                   | 3.41 ms                                                | 3.44 ms: 1.01x slower                                  |
| comprehensions          | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| regex_effbot            | 2.63 ms                                                | 2.67 ms: 1.01x slower                                  |
| pprint_pformat          | 954 ms                                                 | 968 ms: 1.01x slower                                   |
| xml_etree_iterparse     | 70.1 ms                                                | 71.2 ms: 1.01x slower                                  |
| json_loads              | 16.1 us                                                | 16.4 us: 1.02x slower                                  |
| docutils                | 1.47 sec                                               | 1.50 sec: 1.02x slower                                 |
| pprint_safe_repr        | 466 ms                                                 | 475 ms: 1.02x slower                                   |
| pickle_list             | 2.81 us                                                | 2.87 us: 1.02x slower                                  |
| sympy_integrate         | 11.5 ms                                                | 11.8 ms: 1.02x slower                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 545 ms: 1.02x slower                                   |
| deepcopy_reduce         | 1.91 us                                                | 1.95 us: 1.02x slower                                  |
| pickle_dict             | 18.0 us                                                | 18.4 us: 1.02x slower                                  |
| fannkuch                | 261 ms                                                 | 269 ms: 1.03x slower                                   |
| sqlglot_normalize       | 171 ms                                                 | 176 ms: 1.03x slower                                   |
| sqlglot_optimize        | 31.1 ms                                                | 32.0 ms: 1.03x slower                                  |
| sympy_str               | 151 ms                                                 | 156 ms: 1.03x slower                                   |
| sqlalchemy_declarative  | 62.6 ms                                                | 64.6 ms: 1.03x slower                                  |
| sympy_expand            | 242 ms                                                 | 250 ms: 1.03x slower                                   |
| bench_mp_pool           | 43.9 ms                                                | 45.4 ms: 1.03x slower                                  |
| pathlib                 | 27.2 ms                                                | 28.1 ms: 1.03x slower                                  |
| django_template         | 21.0 ms                                                | 21.7 ms: 1.03x slower                                  |
| sympy_sum               | 85.5 ms                                                | 88.6 ms: 1.04x slower                                  |
| thrift                  | 442 us                                                 | 458 us: 1.04x slower                                   |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.47 ms: 1.04x slower                                  |
| 2to3                    | 161 ms                                                 | 168 ms: 1.04x slower                                   |
| coverage                | 58.4 ms                                                | 60.9 ms: 1.04x slower                                  |
| async_tree_io           | 704 ms                                                 | 735 ms: 1.04x slower                                   |
| logging_simple          | 3.55 us                                                | 3.71 us: 1.04x slower                                  |
| xml_etree_process       | 35.1 ms                                                | 36.8 ms: 1.05x slower                                  |
| pickle                  | 7.15 us                                                | 7.52 us: 1.05x slower                                  |
| html5lib                | 34.7 ms                                                | 36.6 ms: 1.05x slower                                  |
| crypto_pyaes            | 51.7 ms                                                | 54.7 ms: 1.06x slower                                  |
| coroutines              | 17.8 ms                                                | 18.8 ms: 1.06x slower                                  |
| nqueens                 | 59.8 ms                                                | 63.4 ms: 1.06x slower                                  |
| go                      | 109 ms                                                 | 116 ms: 1.07x slower                                   |
| scimark_sor             | 82.6 ms                                                | 88.2 ms: 1.07x slower                                  |
| xml_etree_generate      | 48.3 ms                                                | 51.5 ms: 1.07x slower                                  |
| raytrace                | 207 ms                                                 | 221 ms: 1.07x slower                                   |
| logging_format          | 3.78 us                                                | 4.05 us: 1.07x slower                                  |
| sqlite_synth            | 1.27 us                                                | 1.37 us: 1.08x slower                                  |
| pyflate                 | 310 ms                                                 | 342 ms: 1.10x slower                                   |
| scimark_monte_carlo     | 46.5 ms                                                | 52.5 ms: 1.13x slower                                  |
| async_generators        | 196 ms                                                 | 264 ms: 1.34x slower                                   |
| mypy2                   | 195 ms                                                 | 265 ms: 1.36x slower                                   |
| Geometric mean          | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (6): tornado_http, async_tree_memoization, regex_compile, float, async_tree_none, deepcopy
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230408-3.12.0a7+-3516704/bm-20230408-darwin-arm64-python-main-3.12.0a7+-3516704.json: dask


# HPT report

- Reliability score: 98.69% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
