
# Results vs. 3.11.0

- fork: python
- ref: 5b3a2569f4b4dfb58a8f
- machine: darwin-arm64
- commit hash: 5b3a256
- commit date: 2022-09-19
- overall geometric mean: 1.00x slower \*
- HPT reliability: 98.89%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| chameleon      | 4.60 ms                                                | 4.69 ms: 1.02x slower                                                 |
| docutils       | 1.47 sec                                               | 1.48 sec: 1.00x slower                                                |
| html5lib       | 34.7 ms                                                | 35.8 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| float          | 53.0 ms                                                | 55.9 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.6 ms: 1.02x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.67 ms: 1.02x slower                                                 |
| regex_dna      | 152 ms                                                 | 155 ms: 1.02x slower                                                  |
| regex_v8       | 16.1 ms                                                | 16.7 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.09 ms: 1.25x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 96.1 ms: 1.12x faster                                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 64.8 ms: 1.08x faster                                                 |
| unpickle_list        | 2.65 us                                                | 2.54 us: 1.04x faster                                                 |
| xml_etree_generate   | 48.3 ms                                                | 47.5 ms: 1.02x faster                                                 |
| pickle_dict          | 18.0 us                                                | 17.9 us: 1.00x faster                                                 |
| xml_etree_process    | 35.1 ms                                                | 34.9 ms: 1.00x faster                                                 |
| pickle_list          | 2.81 us                                                | 2.83 us: 1.01x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 161 us: 1.01x slower                                                  |
| pickle_pure_python   | 201 us                                                 | 206 us: 1.03x slower                                                  |
| pickle               | 7.15 us                                                | 7.52 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 7.30 ms: 1.39x faster                                                 |
| python_startup         | 12.4 ms                                                | 9.22 ms: 1.35x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 8.14 ms: 1.05x faster                                                 |
| genshi_xml      | 29.8 ms                                                | 30.1 ms: 1.01x slower                                                 |
| django_template | 21.0 ms                                                | 21.8 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site  | 10.2 ms                                                | 7.30 ms: 1.39x faster                                                 |
| python_startup          | 12.4 ms                                                | 9.22 ms: 1.35x faster                                                 |
| pathlib                 | 27.2 ms                                                | 20.6 ms: 1.32x faster                                                 |
| json_dumps              | 7.63 ms                                                | 6.09 ms: 1.25x faster                                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.83 ms: 1.13x faster                                                 |
| xml_etree_parse         | 108 ms                                                 | 96.1 ms: 1.12x faster                                                 |
| coverage                | 58.4 ms                                                | 53.3 ms: 1.10x faster                                                 |
| flaskblogging           | 2.43 ms                                                | 2.24 ms: 1.08x faster                                                 |
| xml_etree_iterparse     | 70.1 ms                                                | 64.8 ms: 1.08x faster                                                 |
| bench_mp_pool           | 43.9 ms                                                | 41.4 ms: 1.06x faster                                                 |
| mako                    | 8.53 ms                                                | 8.14 ms: 1.05x faster                                                 |
| bench_thread_pool       | 474 us                                                 | 455 us: 1.04x faster                                                  |
| unpickle_list           | 2.65 us                                                | 2.54 us: 1.04x faster                                                 |
| dulwich_log             | 30.3 ms                                                | 29.1 ms: 1.04x faster                                                 |
| pylint                  | 272 ms                                                 | 264 ms: 1.03x faster                                                  |
| logging_silent          | 68.1 ns                                                | 66.5 ns: 1.02x faster                                                 |
| sqlalchemy_declarative  | 62.6 ms                                                | 61.3 ms: 1.02x faster                                                 |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.07 ms: 1.02x faster                                                 |
| xml_etree_generate      | 48.3 ms                                                | 47.5 ms: 1.02x faster                                                 |
| regex_compile           | 76.7 ms                                                | 75.6 ms: 1.02x faster                                                 |
| telco                   | 3.41 ms                                                | 3.36 ms: 1.01x faster                                                 |
| mdp                     | 1.55 sec                                               | 1.53 sec: 1.01x faster                                                |
| scimark_lu              | 73.3 ms                                                | 72.4 ms: 1.01x faster                                                 |
| async_tree_none         | 286 ms                                                 | 282 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 529 ms: 1.01x faster                                                  |
| pickle_dict             | 18.0 us                                                | 17.9 us: 1.00x faster                                                 |
| xml_etree_process       | 35.1 ms                                                | 34.9 ms: 1.00x faster                                                 |
| scimark_fft             | 200 ms                                                 | 199 ms: 1.00x faster                                                  |
| thrift                  | 442 us                                                 | 443 us: 1.00x slower                                                  |
| docutils                | 1.47 sec                                               | 1.48 sec: 1.00x slower                                                |
| spectral_norm           | 72.6 ms                                                | 72.9 ms: 1.00x slower                                                 |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| crypto_pyaes            | 51.7 ms                                                | 52.0 ms: 1.01x slower                                                 |
| deltablue               | 2.81 ms                                                | 2.83 ms: 1.01x slower                                                 |
| sympy_sum               | 85.5 ms                                                | 86.1 ms: 1.01x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.83 us: 1.01x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 161 us: 1.01x slower                                                  |
| genshi_xml              | 29.8 ms                                                | 30.1 ms: 1.01x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.7 ms: 1.01x slower                                                 |
| generators              | 28.8 ms                                                | 29.2 ms: 1.01x slower                                                 |
| regex_effbot            | 2.63 ms                                                | 2.67 ms: 1.02x slower                                                 |
| sympy_str               | 151 ms                                                 | 154 ms: 1.02x slower                                                  |
| chameleon               | 4.60 ms                                                | 4.69 ms: 1.02x slower                                                 |
| regex_dna               | 152 ms                                                 | 155 ms: 1.02x slower                                                  |
| sqlglot_normalize       | 171 ms                                                 | 174 ms: 1.02x slower                                                  |
| json                    | 2.78 ms                                                | 2.84 ms: 1.02x slower                                                 |
| pycparser               | 698 ms                                                 | 713 ms: 1.02x slower                                                  |
| async_generators        | 196 ms                                                 | 201 ms: 1.02x slower                                                  |
| sqlglot_optimize        | 31.1 ms                                                | 31.9 ms: 1.02x slower                                                 |
| nqueens                 | 59.8 ms                                                | 61.2 ms: 1.02x slower                                                 |
| chaos                   | 49.4 ms                                                | 50.7 ms: 1.03x slower                                                 |
| sympy_expand            | 242 ms                                                 | 248 ms: 1.03x slower                                                  |
| pickle_pure_python      | 201 us                                                 | 206 us: 1.03x slower                                                  |
| logging_simple          | 3.55 us                                                | 3.65 us: 1.03x slower                                                 |
| html5lib                | 34.7 ms                                                | 35.8 ms: 1.03x slower                                                 |
| richards                | 32.2 ms                                                | 33.3 ms: 1.03x slower                                                 |
| raytrace                | 207 ms                                                 | 215 ms: 1.04x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.17 ms: 1.04x slower                                                 |
| django_template         | 21.0 ms                                                | 21.8 ms: 1.04x slower                                                 |
| regex_v8                | 16.1 ms                                                | 16.7 ms: 1.04x slower                                                 |
| async_tree_io           | 704 ms                                                 | 732 ms: 1.04x slower                                                  |
| fannkuch                | 261 ms                                                 | 272 ms: 1.04x slower                                                  |
| hexiom                  | 4.72 ms                                                | 4.92 ms: 1.04x slower                                                 |
| logging_format          | 3.78 us                                                | 3.94 us: 1.04x slower                                                 |
| sqlglot_parse           | 959 us                                                 | 1.00 ms: 1.04x slower                                                 |
| pickle                  | 7.15 us                                                | 7.52 us: 1.05x slower                                                 |
| float                   | 53.0 ms                                                | 55.9 ms: 1.06x slower                                                 |
| meteor_contest          | 73.5 ms                                                | 77.9 ms: 1.06x slower                                                 |
| pprint_pformat          | 954 ms                                                 | 1.01 sec: 1.06x slower                                                |
| pprint_safe_repr        | 466 ms                                                 | 496 ms: 1.06x slower                                                  |
| deepcopy                | 223 us                                                 | 240 us: 1.08x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.07 us: 1.08x slower                                                 |
| deepcopy_memo           | 26.3 us                                                | 28.7 us: 1.09x slower                                                 |
| go                      | 109 ms                                                 | 118 ms: 1.09x slower                                                  |
| coroutines              | 17.8 ms                                                | 19.5 ms: 1.10x slower                                                 |
| pyflate                 | 310 ms                                                 | 350 ms: 1.13x slower                                                  |
| async_tree_memoization  | 336 ms                                                 | 381 ms: 1.14x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.45 us: 1.14x slower                                                 |
| 2to3                    | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 54.4 ms: 1.17x slower                                                 |
| scimark_sor             | 82.6 ms                                                | 101 ms: 1.23x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (6): tornado_http, nbody, unpickle, genshi_text, unpack_sequence, json_loads
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, gc_traversal, gunicorn, mypy2, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20220919-3.12.0a0-5b3a256/bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256.json: mypy


# HPT report

- Reliability score: 98.89% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
