
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 432117c
- commit date: 2022-12-16
- overall geometric mean: 1.03x faster \*
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 184 ms: 1.14x slower                                   |
| chameleon      | 4.60 ms                                                | 4.29 ms: 1.07x faster                                  |
| docutils       | 1.47 sec                                               | 1.44 sec: 1.02x faster                                 |
| html5lib       | 34.7 ms                                                | 33.2 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 62.3 ms: 1.05x faster                                  |
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| float          | 53.0 ms                                                | 53.4 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 72.7 ms: 1.06x faster                                  |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| regex_v8       | 16.1 ms                                                | 16.0 ms: 1.01x faster                                  |
| regex_effbot   | 2.63 ms                                                | 2.71 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.16 ms: 1.24x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 92.9 ms: 1.16x faster                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 65.5 ms: 1.07x faster                                  |
| unpickle_pure_python | 159 us                                                 | 151 us: 1.05x faster                                   |
| unpickle_list        | 2.65 us                                                | 2.56 us: 1.04x faster                                  |
| xml_etree_generate   | 48.3 ms                                                | 47.0 ms: 1.03x faster                                  |
| xml_etree_process    | 35.1 ms                                                | 34.4 ms: 1.02x faster                                  |
| pickle_pure_python   | 201 us                                                 | 197 us: 1.02x faster                                   |
| pickle_dict          | 18.0 us                                                | 18.0 us: 1.00x slower                                  |
| pickle_list          | 2.81 us                                                | 2.84 us: 1.01x slower                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| unpickle             | 9.67 us                                                | 9.84 us: 1.02x slower                                  |
| pickle               | 7.15 us                                                | 7.55 us: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 7.34 ms: 1.38x faster                                  |
| python_startup         | 12.4 ms                                                | 9.29 ms: 1.34x faster                                  |
| Geometric mean         | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.53 ms                                                | 6.96 ms: 1.23x faster                                  |
| genshi_text     | 15.3 ms                                                | 13.9 ms: 1.10x faster                                  |
| genshi_xml      | 29.8 ms                                                | 28.2 ms: 1.06x faster                                  |
| django_template | 21.0 ms                                                | 20.7 ms: 1.02x faster                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site  | 10.2 ms                                                | 7.34 ms: 1.38x faster                                  |
| python_startup          | 12.4 ms                                                | 9.29 ms: 1.34x faster                                  |
| pathlib                 | 27.2 ms                                                | 20.4 ms: 1.34x faster                                  |
| json_dumps              | 7.63 ms                                                | 6.16 ms: 1.24x faster                                  |
| mako                    | 8.53 ms                                                | 6.96 ms: 1.23x faster                                  |
| xml_etree_parse         | 108 ms                                                 | 92.9 ms: 1.16x faster                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.77 ms: 1.15x faster                                  |
| unpack_sequence         | 34.1 ns                                                | 30.4 ns: 1.12x faster                                  |
| deltablue               | 2.81 ms                                                | 2.51 ms: 1.12x faster                                  |
| richards                | 32.2 ms                                                | 29.2 ms: 1.10x faster                                  |
| genshi_text             | 15.3 ms                                                | 13.9 ms: 1.10x faster                                  |
| logging_silent          | 68.1 ns                                                | 62.7 ns: 1.09x faster                                  |
| chameleon               | 4.60 ms                                                | 4.29 ms: 1.07x faster                                  |
| xml_etree_iterparse     | 70.1 ms                                                | 65.5 ms: 1.07x faster                                  |
| dulwich_log             | 30.3 ms                                                | 28.4 ms: 1.07x faster                                  |
| bench_thread_pool       | 474 us                                                 | 445 us: 1.07x faster                                   |
| coverage                | 58.4 ms                                                | 54.9 ms: 1.06x faster                                  |
| scimark_lu              | 73.3 ms                                                | 69.0 ms: 1.06x faster                                  |
| scimark_sor             | 82.6 ms                                                | 78.1 ms: 1.06x faster                                  |
| genshi_xml              | 29.8 ms                                                | 28.2 ms: 1.06x faster                                  |
| regex_compile           | 76.7 ms                                                | 72.7 ms: 1.06x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 151 us: 1.05x faster                                   |
| nbody                   | 65.6 ms                                                | 62.3 ms: 1.05x faster                                  |
| pycparser               | 698 ms                                                 | 665 ms: 1.05x faster                                   |
| html5lib                | 34.7 ms                                                | 33.2 ms: 1.05x faster                                  |
| unpickle_list           | 2.65 us                                                | 2.56 us: 1.04x faster                                  |
| scimark_fft             | 200 ms                                                 | 193 ms: 1.04x faster                                   |
| mdp                     | 1.55 sec                                               | 1.50 sec: 1.03x faster                                 |
| logging_simple          | 3.55 us                                                | 3.44 us: 1.03x faster                                  |
| hexiom                  | 4.72 ms                                                | 4.59 ms: 1.03x faster                                  |
| xml_etree_generate      | 48.3 ms                                                | 47.0 ms: 1.03x faster                                  |
| fannkuch                | 261 ms                                                 | 255 ms: 1.03x faster                                   |
| go                      | 109 ms                                                 | 106 ms: 1.02x faster                                   |
| docutils                | 1.47 sec                                               | 1.44 sec: 1.02x faster                                 |
| thrift                  | 442 us                                                 | 433 us: 1.02x faster                                   |
| sqlglot_normalize       | 171 ms                                                 | 167 ms: 1.02x faster                                   |
| raytrace                | 207 ms                                                 | 203 ms: 1.02x faster                                   |
| xml_etree_process       | 35.1 ms                                                | 34.4 ms: 1.02x faster                                  |
| coroutines              | 17.8 ms                                                | 17.4 ms: 1.02x faster                                  |
| chaos                   | 49.4 ms                                                | 48.6 ms: 1.02x faster                                  |
| django_template         | 21.0 ms                                                | 20.7 ms: 1.02x faster                                  |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| sympy_integrate         | 11.5 ms                                                | 11.3 ms: 1.02x faster                                  |
| telco                   | 3.41 ms                                                | 3.35 ms: 1.02x faster                                  |
| pickle_pure_python      | 201 us                                                 | 197 us: 1.02x faster                                   |
| spectral_norm           | 72.6 ms                                                | 71.7 ms: 1.01x faster                                  |
| logging_format          | 3.78 us                                                | 3.74 us: 1.01x faster                                  |
| sympy_str               | 151 ms                                                 | 150 ms: 1.01x faster                                   |
| sqlglot_optimize        | 31.1 ms                                                | 30.8 ms: 1.01x faster                                  |
| nqueens                 | 59.8 ms                                                | 59.3 ms: 1.01x faster                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 46.1 ms: 1.01x faster                                  |
| sympy_expand            | 242 ms                                                 | 240 ms: 1.01x faster                                   |
| sympy_sum               | 85.5 ms                                                | 85.0 ms: 1.01x faster                                  |
| regex_v8                | 16.1 ms                                                | 16.0 ms: 1.01x faster                                  |
| pickle_dict             | 18.0 us                                                | 18.0 us: 1.00x slower                                  |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| pprint_safe_repr        | 466 ms                                                 | 470 ms: 1.01x slower                                   |
| float                   | 53.0 ms                                                | 53.4 ms: 1.01x slower                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 538 ms: 1.01x slower                                   |
| pickle_list             | 2.81 us                                                | 2.84 us: 1.01x slower                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.14 ms: 1.01x slower                                  |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| json                    | 2.78 ms                                                | 2.82 ms: 1.02x slower                                  |
| unpickle                | 9.67 us                                                | 9.84 us: 1.02x slower                                  |
| sqlglot_parse           | 959 us                                                 | 976 us: 1.02x slower                                   |
| deepcopy                | 223 us                                                 | 227 us: 1.02x slower                                   |
| deepcopy_reduce         | 1.91 us                                                | 1.95 us: 1.02x slower                                  |
| async_generators        | 196 ms                                                 | 201 ms: 1.02x slower                                   |
| crypto_pyaes            | 51.7 ms                                                | 53.0 ms: 1.02x slower                                  |
| meteor_contest          | 73.5 ms                                                | 75.4 ms: 1.03x slower                                  |
| regex_effbot            | 2.63 ms                                                | 2.71 ms: 1.03x slower                                  |
| async_tree_io           | 704 ms                                                 | 732 ms: 1.04x slower                                   |
| deepcopy_memo           | 26.3 us                                                | 27.4 us: 1.04x slower                                  |
| pyflate                 | 310 ms                                                 | 324 ms: 1.05x slower                                   |
| pickle                  | 7.15 us                                                | 7.55 us: 1.06x slower                                  |
| generators              | 28.8 ms                                                | 32.2 ms: 1.12x slower                                  |
| sqlite_synth            | 1.27 us                                                | 1.43 us: 1.13x slower                                  |
| 2to3                    | 161 ms                                                 | 184 ms: 1.14x slower                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_none, bench_mp_pool, pprint_pformat
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221216-3.12.0a3+-432117c/bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c.json: mypy


# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
