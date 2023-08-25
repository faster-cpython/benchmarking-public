
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 951303f
- commit date: 2023-01-07
- overall geometric mean: 1.02x faster \*
- HPT reliability: 95.91%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 182 ms: 1.13x slower                                   |
| chameleon      | 4.60 ms                                                | 4.48 ms: 1.03x faster                                  |
| docutils       | 1.47 sec                                               | 1.43 sec: 1.03x faster                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 63.8 ms: 1.03x faster                                  |
| float          | 53.0 ms                                                | 51.6 ms: 1.03x faster                                  |
| pidigits       | 281 ms                                                 | 277 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.2 ms: 1.02x faster                                  |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                  |
| regex_v8       | 16.1 ms                                                | 16.1 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.10 ms: 1.25x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 92.8 ms: 1.16x faster                                  |
| unpickle_pure_python | 159 us                                                 | 142 us: 1.12x faster                                   |
| unpickle             | 9.67 us                                                | 9.05 us: 1.07x faster                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 66.2 ms: 1.06x faster                                  |
| pickle_pure_python   | 201 us                                                 | 192 us: 1.04x faster                                   |
| xml_etree_process    | 35.1 ms                                                | 34.7 ms: 1.01x faster                                  |
| unpickle_list        | 2.65 us                                                | 2.63 us: 1.01x faster                                  |
| xml_etree_generate   | 48.3 ms                                                | 48.5 ms: 1.00x slower                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| pickle_list          | 2.81 us                                                | 2.86 us: 1.02x slower                                  |
| pickle               | 7.15 us                                                | 7.52 us: 1.05x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 7.32 ms: 1.39x faster                                  |
| python_startup         | 12.4 ms                                                | 9.28 ms: 1.34x faster                                  |
| Geometric mean         | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.10 ms: 1.20x faster                                  |
| genshi_text     | 15.3 ms                                                | 14.3 ms: 1.07x faster                                  |
| genshi_xml      | 29.8 ms                                                | 28.2 ms: 1.06x faster                                  |
| django_template | 21.0 ms                                                | 21.3 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site  | 10.2 ms                                                | 7.32 ms: 1.39x faster                                  |
| python_startup          | 12.4 ms                                                | 9.28 ms: 1.34x faster                                  |
| pathlib                 | 27.2 ms                                                | 20.8 ms: 1.31x faster                                  |
| json_dumps              | 7.63 ms                                                | 6.10 ms: 1.25x faster                                  |
| mako                    | 8.53 ms                                                | 7.10 ms: 1.20x faster                                  |
| xml_etree_parse         | 108 ms                                                 | 92.8 ms: 1.16x faster                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.82 ms: 1.13x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 142 us: 1.12x faster                                   |
| deltablue               | 2.81 ms                                                | 2.56 ms: 1.10x faster                                  |
| genshi_text             | 15.3 ms                                                | 14.3 ms: 1.07x faster                                  |
| unpickle                | 9.67 us                                                | 9.05 us: 1.07x faster                                  |
| richards                | 32.2 ms                                                | 30.4 ms: 1.06x faster                                  |
| xml_etree_iterparse     | 70.1 ms                                                | 66.2 ms: 1.06x faster                                  |
| genshi_xml              | 29.8 ms                                                | 28.2 ms: 1.06x faster                                  |
| dulwich_log             | 30.3 ms                                                | 28.7 ms: 1.06x faster                                  |
| bench_thread_pool       | 474 us                                                 | 450 us: 1.05x faster                                   |
| logging_silent          | 68.1 ns                                                | 64.9 ns: 1.05x faster                                  |
| unpack_sequence         | 34.1 ns                                                | 32.5 ns: 1.05x faster                                  |
| bench_mp_pool           | 43.9 ms                                                | 41.9 ms: 1.05x faster                                  |
| pickle_pure_python      | 201 us                                                 | 192 us: 1.04x faster                                   |
| pprint_pformat          | 954 ms                                                 | 925 ms: 1.03x faster                                   |
| deepcopy_memo           | 26.3 us                                                | 25.6 us: 1.03x faster                                  |
| nbody                   | 65.6 ms                                                | 63.8 ms: 1.03x faster                                  |
| docutils                | 1.47 sec                                               | 1.43 sec: 1.03x faster                                 |
| chameleon               | 4.60 ms                                                | 4.48 ms: 1.03x faster                                  |
| float                   | 53.0 ms                                                | 51.6 ms: 1.03x faster                                  |
| pprint_safe_repr        | 466 ms                                                 | 455 ms: 1.02x faster                                   |
| async_tree_memoization  | 336 ms                                                 | 328 ms: 1.02x faster                                   |
| scimark_fft             | 200 ms                                                 | 195 ms: 1.02x faster                                   |
| regex_compile           | 76.7 ms                                                | 75.2 ms: 1.02x faster                                  |
| scimark_lu              | 73.3 ms                                                | 71.9 ms: 1.02x faster                                  |
| coverage                | 58.4 ms                                                | 57.3 ms: 1.02x faster                                  |
| pycparser               | 698 ms                                                 | 685 ms: 1.02x faster                                   |
| deepcopy                | 223 us                                                 | 219 us: 1.02x faster                                   |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| pidigits                | 281 ms                                                 | 277 ms: 1.01x faster                                   |
| fannkuch                | 261 ms                                                 | 258 ms: 1.01x faster                                   |
| sympy_integrate         | 11.5 ms                                                | 11.4 ms: 1.01x faster                                  |
| xml_etree_process       | 35.1 ms                                                | 34.7 ms: 1.01x faster                                  |
| regex_effbot            | 2.63 ms                                                | 2.61 ms: 1.01x faster                                  |
| go                      | 109 ms                                                 | 108 ms: 1.01x faster                                   |
| logging_simple          | 3.55 us                                                | 3.52 us: 1.01x faster                                  |
| mdp                     | 1.55 sec                                               | 1.53 sec: 1.01x faster                                 |
| unpickle_list           | 2.65 us                                                | 2.63 us: 1.01x faster                                  |
| thrift                  | 442 us                                                 | 439 us: 1.01x faster                                   |
| sqlglot_normalize       | 171 ms                                                 | 170 ms: 1.01x faster                                   |
| sympy_expand            | 242 ms                                                 | 241 ms: 1.00x faster                                   |
| sqlglot_optimize        | 31.1 ms                                                | 31.0 ms: 1.00x faster                                  |
| regex_v8                | 16.1 ms                                                | 16.1 ms: 1.00x faster                                  |
| scimark_sor             | 82.6 ms                                                | 82.4 ms: 1.00x faster                                  |
| spectral_norm           | 72.6 ms                                                | 72.8 ms: 1.00x slower                                  |
| xml_etree_generate      | 48.3 ms                                                | 48.5 ms: 1.00x slower                                  |
| sympy_sum               | 85.5 ms                                                | 85.9 ms: 1.00x slower                                  |
| nqueens                 | 59.8 ms                                                | 60.2 ms: 1.01x slower                                  |
| logging_format          | 3.78 us                                                | 3.81 us: 1.01x slower                                  |
| hexiom                  | 4.72 ms                                                | 4.78 ms: 1.01x slower                                  |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| django_template         | 21.0 ms                                                | 21.3 ms: 1.01x slower                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 541 ms: 1.01x slower                                   |
| pickle_list             | 2.81 us                                                | 2.86 us: 1.02x slower                                  |
| telco                   | 3.41 ms                                                | 3.47 ms: 1.02x slower                                  |
| chaos                   | 49.4 ms                                                | 50.3 ms: 1.02x slower                                  |
| async_generators        | 196 ms                                                 | 200 ms: 1.02x slower                                   |
| json                    | 2.78 ms                                                | 2.84 ms: 1.02x slower                                  |
| pyflate                 | 310 ms                                                 | 322 ms: 1.04x slower                                   |
| meteor_contest          | 73.5 ms                                                | 76.3 ms: 1.04x slower                                  |
| crypto_pyaes            | 51.7 ms                                                | 53.7 ms: 1.04x slower                                  |
| async_tree_io           | 704 ms                                                 | 736 ms: 1.04x slower                                   |
| pickle                  | 7.15 us                                                | 7.52 us: 1.05x slower                                  |
| coroutines              | 17.8 ms                                                | 18.8 ms: 1.06x slower                                  |
| sqlite_synth            | 1.27 us                                                | 1.35 us: 1.06x slower                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.20 ms: 1.07x slower                                  |
| raytrace                | 207 ms                                                 | 221 ms: 1.07x slower                                   |
| sqlglot_parse           | 959 us                                                 | 1.04 ms: 1.08x slower                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 51.0 ms: 1.10x slower                                  |
| 2to3                    | 161 ms                                                 | 182 ms: 1.13x slower                                   |
| generators              | 28.8 ms                                                | 33.7 ms: 1.17x slower                                  |
| Geometric mean          | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (5): deepcopy_reduce, html5lib, pickle_dict, sympy_str, async_tree_none
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230107-3.12.0a3+-951303f/bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f.json: mypy


# HPT report

- Reliability score: 95.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
