
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 3eb12df
- commit date: 2023-02-11
- overall geometric mean: 1.03x faster \*
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 181 ms: 1.12x slower                                   |
| chameleon      | 4.60 ms                                                | 4.34 ms: 1.06x faster                                  |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.00x faster                                 |
| tornado_http   | 71.5 ms                                                | 68.4 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 53.0 ms                                                | 49.7 ms: 1.07x faster                                  |
| nbody          | 65.6 ms                                                | 63.1 ms: 1.04x faster                                  |
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 71.0 ms: 1.08x faster                                  |
| regex_dna      | 152 ms                                                 | 150 ms: 1.02x faster                                   |
| regex_effbot   | 2.63 ms                                                | 2.60 ms: 1.01x faster                                  |
| regex_v8       | 16.1 ms                                                | 16.0 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.06 ms: 1.26x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 93.0 ms: 1.16x faster                                  |
| unpickle_pure_python | 159 us                                                 | 137 us: 1.16x faster                                   |
| pickle_pure_python   | 201 us                                                 | 185 us: 1.09x faster                                   |
| xml_etree_iterparse  | 70.1 ms                                                | 67.1 ms: 1.05x faster                                  |
| xml_etree_process    | 35.1 ms                                                | 35.2 ms: 1.00x slower                                  |
| pickle_list          | 2.81 us                                                | 2.83 us: 1.01x slower                                  |
| unpickle_list        | 2.65 us                                                | 2.67 us: 1.01x slower                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.02x slower                                  |
| xml_etree_generate   | 48.3 ms                                                | 49.2 ms: 1.02x slower                                  |
| unpickle             | 9.67 us                                                | 9.91 us: 1.02x slower                                  |
| pickle               | 7.15 us                                                | 7.57 us: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 7.38 ms: 1.38x faster                                  |
| python_startup         | 12.4 ms                                                | 9.36 ms: 1.33x faster                                  |
| Geometric mean         | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.13 ms: 1.20x faster                                  |
| genshi_text     | 15.3 ms                                                | 13.8 ms: 1.11x faster                                  |
| genshi_xml      | 29.8 ms                                                | 27.5 ms: 1.08x faster                                  |
| django_template | 21.0 ms                                                | 20.8 ms: 1.01x faster                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230211-darwin-arm64-python-main-3.12.0a5+-3eb12df |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 411 ms: 1.58x faster                                   |
| python_startup_no_site  | 10.2 ms                                                | 7.38 ms: 1.38x faster                                  |
| python_startup          | 12.4 ms                                                | 9.36 ms: 1.33x faster                                  |
| json_dumps              | 7.63 ms                                                | 6.06 ms: 1.26x faster                                  |
| pathlib                 | 27.2 ms                                                | 21.8 ms: 1.25x faster                                  |
| mako                    | 8.53 ms                                                | 7.13 ms: 1.20x faster                                  |
| xml_etree_parse         | 108 ms                                                 | 93.0 ms: 1.16x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 137 us: 1.16x faster                                   |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.77 ms: 1.15x faster                                  |
| deltablue               | 2.81 ms                                                | 2.47 ms: 1.14x faster                                  |
| hexiom                  | 4.72 ms                                                | 4.21 ms: 1.12x faster                                  |
| unpack_sequence         | 34.1 ns                                                | 30.6 ns: 1.12x faster                                  |
| genshi_text             | 15.3 ms                                                | 13.8 ms: 1.11x faster                                  |
| richards                | 32.2 ms                                                | 29.5 ms: 1.09x faster                                  |
| chaos                   | 49.4 ms                                                | 45.5 ms: 1.09x faster                                  |
| pickle_pure_python      | 201 us                                                 | 185 us: 1.09x faster                                   |
| genshi_xml              | 29.8 ms                                                | 27.5 ms: 1.08x faster                                  |
| regex_compile           | 76.7 ms                                                | 71.0 ms: 1.08x faster                                  |
| dulwich_log             | 30.3 ms                                                | 28.4 ms: 1.07x faster                                  |
| bench_thread_pool       | 474 us                                                 | 444 us: 1.07x faster                                   |
| float                   | 53.0 ms                                                | 49.7 ms: 1.07x faster                                  |
| deepcopy_memo           | 26.3 us                                                | 24.7 us: 1.06x faster                                  |
| logging_silent          | 68.1 ns                                                | 64.1 ns: 1.06x faster                                  |
| chameleon               | 4.60 ms                                                | 4.34 ms: 1.06x faster                                  |
| scimark_fft             | 200 ms                                                 | 189 ms: 1.05x faster                                   |
| pycparser               | 698 ms                                                 | 664 ms: 1.05x faster                                   |
| async_tree_memoization  | 336 ms                                                 | 320 ms: 1.05x faster                                   |
| sympy_str               | 151 ms                                                 | 144 ms: 1.05x faster                                   |
| xml_etree_iterparse     | 70.1 ms                                                | 67.1 ms: 1.05x faster                                  |
| tornado_http            | 71.5 ms                                                | 68.4 ms: 1.05x faster                                  |
| sympy_sum               | 85.5 ms                                                | 82.1 ms: 1.04x faster                                  |
| create_gc_cycles        | 716 us                                                 | 687 us: 1.04x faster                                   |
| fannkuch                | 261 ms                                                 | 251 ms: 1.04x faster                                   |
| scimark_lu              | 73.3 ms                                                | 70.5 ms: 1.04x faster                                  |
| nbody                   | 65.6 ms                                                | 63.1 ms: 1.04x faster                                  |
| pprint_pformat          | 954 ms                                                 | 920 ms: 1.04x faster                                   |
| deepcopy                | 223 us                                                 | 215 us: 1.04x faster                                   |
| sympy_integrate         | 11.5 ms                                                | 11.1 ms: 1.04x faster                                  |
| pprint_safe_repr        | 466 ms                                                 | 452 ms: 1.03x faster                                   |
| bench_mp_pool           | 43.9 ms                                                | 42.6 ms: 1.03x faster                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.86 us: 1.03x faster                                  |
| async_tree_none         | 286 ms                                                 | 278 ms: 1.03x faster                                   |
| mdp                     | 1.55 sec                                               | 1.51 sec: 1.02x faster                                 |
| regex_dna               | 152 ms                                                 | 150 ms: 1.02x faster                                   |
| sympy_expand            | 242 ms                                                 | 238 ms: 1.02x faster                                   |
| go                      | 109 ms                                                 | 107 ms: 1.01x faster                                   |
| django_template         | 21.0 ms                                                | 20.8 ms: 1.01x faster                                  |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.12 ms: 1.01x faster                                  |
| meteor_contest          | 73.5 ms                                                | 72.7 ms: 1.01x faster                                  |
| sqlglot_normalize       | 171 ms                                                 | 169 ms: 1.01x faster                                   |
| regex_effbot            | 2.63 ms                                                | 2.60 ms: 1.01x faster                                  |
| logging_simple          | 3.55 us                                                | 3.51 us: 1.01x faster                                  |
| telco                   | 3.41 ms                                                | 3.38 ms: 1.01x faster                                  |
| nqueens                 | 59.8 ms                                                | 59.5 ms: 1.00x faster                                  |
| gc_traversal            | 2.42 ms                                                | 2.41 ms: 1.00x faster                                  |
| regex_v8                | 16.1 ms                                                | 16.0 ms: 1.00x faster                                  |
| docutils                | 1.47 sec                                               | 1.46 sec: 1.00x faster                                 |
| xml_etree_process       | 35.1 ms                                                | 35.2 ms: 1.00x slower                                  |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| logging_format          | 3.78 us                                                | 3.80 us: 1.00x slower                                  |
| pickle_list             | 2.81 us                                                | 2.83 us: 1.01x slower                                  |
| unpickle_list           | 2.65 us                                                | 2.67 us: 1.01x slower                                  |
| scimark_sor             | 82.6 ms                                                | 83.4 ms: 1.01x slower                                  |
| spectral_norm           | 72.6 ms                                                | 73.4 ms: 1.01x slower                                  |
| thrift                  | 442 us                                                 | 447 us: 1.01x slower                                   |
| json_loads              | 16.1 us                                                | 16.3 us: 1.02x slower                                  |
| json                    | 2.78 ms                                                | 2.83 ms: 1.02x slower                                  |
| xml_etree_generate      | 48.3 ms                                                | 49.2 ms: 1.02x slower                                  |
| unpickle                | 9.67 us                                                | 9.91 us: 1.02x slower                                  |
| async_tree_io           | 704 ms                                                 | 726 ms: 1.03x slower                                   |
| coverage                | 58.4 ms                                                | 60.3 ms: 1.03x slower                                  |
| crypto_pyaes            | 51.7 ms                                                | 53.4 ms: 1.03x slower                                  |
| coroutines              | 17.8 ms                                                | 18.4 ms: 1.03x slower                                  |
| pyflate                 | 310 ms                                                 | 324 ms: 1.04x slower                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.18 ms: 1.05x slower                                  |
| raytrace                | 207 ms                                                 | 217 ms: 1.05x slower                                   |
| sqlglot_parse           | 959 us                                                 | 1.01 ms: 1.05x slower                                  |
| pickle                  | 7.15 us                                                | 7.57 us: 1.06x slower                                  |
| sqlite_synth            | 1.27 us                                                | 1.37 us: 1.08x slower                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 50.0 ms: 1.08x slower                                  |
| 2to3                    | 161 ms                                                 | 181 ms: 1.12x slower                                   |
| generators              | 28.8 ms                                                | 32.9 ms: 1.14x slower                                  |
| async_generators        | 196 ms                                                 | 255 ms: 1.30x slower                                   |
| mypy2                   | 195 ms                                                 | 271 ms: 1.39x slower                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (5): pickle_dict, sqlglot_optimize, sqlalchemy_declarative, async_tree_cpu_io_mixed, html5lib
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
