
# Results vs. 3.11.0

- fork: python
- ref: a0ad63e70e3682cdf7e8
- machine: darwin-arm64
- commit hash: a0ad63e
- commit date: 2022-09-04
- overall geometric mean: 1.01x faster \*
- HPT reliability: 51.69%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 185 ms: 1.14x slower                                                  |
| chameleon      | 4.60 ms                                                | 4.59 ms: 1.00x faster                                                 |
| docutils       | 1.47 sec                                               | 1.48 sec: 1.00x slower                                                |
| html5lib       | 34.7 ms                                                | 36.4 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 51.3 ms: 1.03x faster                                                 |
| nbody          | 65.6 ms                                                | 64.0 ms: 1.02x faster                                                 |
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.3 ms: 1.02x faster                                                 |
| regex_dna      | 152 ms                                                 | 151 ms: 1.00x faster                                                  |
| regex_v8       | 16.1 ms                                                | 16.4 ms: 1.02x slower                                                 |
| regex_effbot   | 2.63 ms                                                | 2.72 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.10 ms: 1.25x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 95.9 ms: 1.13x faster                                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 64.5 ms: 1.09x faster                                                 |
| unpickle_list        | 2.65 us                                                | 2.58 us: 1.03x faster                                                 |
| xml_etree_generate   | 48.3 ms                                                | 47.2 ms: 1.02x faster                                                 |
| xml_etree_process    | 35.1 ms                                                | 34.5 ms: 1.02x faster                                                 |
| pickle_pure_python   | 201 us                                                 | 198 us: 1.01x faster                                                  |
| unpickle_pure_python | 159 us                                                 | 160 us: 1.00x slower                                                  |
| json_loads           | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| pickle_list          | 2.81 us                                                | 2.85 us: 1.01x slower                                                 |
| pickle               | 7.15 us                                                | 7.59 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 7.16 ms: 1.42x faster                                                 |
| python_startup         | 12.4 ms                                                | 9.07 ms: 1.37x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.97 ms: 1.07x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.1 ms: 1.01x faster                                                 |
| django_template | 21.0 ms                                                | 20.9 ms: 1.00x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site  | 10.2 ms                                                | 7.16 ms: 1.42x faster                                                 |
| python_startup          | 12.4 ms                                                | 9.07 ms: 1.37x faster                                                 |
| pathlib                 | 27.2 ms                                                | 20.8 ms: 1.31x faster                                                 |
| json_dumps              | 7.63 ms                                                | 6.10 ms: 1.25x faster                                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.80 ms: 1.14x faster                                                 |
| xml_etree_parse         | 108 ms                                                 | 95.9 ms: 1.13x faster                                                 |
| flaskblogging           | 2.43 ms                                                | 2.22 ms: 1.09x faster                                                 |
| xml_etree_iterparse     | 70.1 ms                                                | 64.5 ms: 1.09x faster                                                 |
| coverage                | 58.4 ms                                                | 54.3 ms: 1.08x faster                                                 |
| bench_mp_pool           | 43.9 ms                                                | 40.9 ms: 1.07x faster                                                 |
| mako                    | 8.53 ms                                                | 7.97 ms: 1.07x faster                                                 |
| deepcopy_memo           | 26.3 us                                                | 24.8 us: 1.06x faster                                                 |
| bench_thread_pool       | 474 us                                                 | 449 us: 1.06x faster                                                  |
| logging_silent          | 68.1 ns                                                | 64.5 ns: 1.06x faster                                                 |
| unpack_sequence         | 34.1 ns                                                | 33.0 ns: 1.04x faster                                                 |
| deepcopy                | 223 us                                                 | 215 us: 1.03x faster                                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.85 us: 1.03x faster                                                 |
| float                   | 53.0 ms                                                | 51.3 ms: 1.03x faster                                                 |
| dulwich_log             | 30.3 ms                                                | 29.5 ms: 1.03x faster                                                 |
| pylint                  | 272 ms                                                 | 264 ms: 1.03x faster                                                  |
| unpickle_list           | 2.65 us                                                | 2.58 us: 1.03x faster                                                 |
| nbody                   | 65.6 ms                                                | 64.0 ms: 1.02x faster                                                 |
| xml_etree_generate      | 48.3 ms                                                | 47.2 ms: 1.02x faster                                                 |
| telco                   | 3.41 ms                                                | 3.34 ms: 1.02x faster                                                 |
| regex_compile           | 76.7 ms                                                | 75.3 ms: 1.02x faster                                                 |
| sympy_sum               | 85.5 ms                                                | 84.0 ms: 1.02x faster                                                 |
| nqueens                 | 59.8 ms                                                | 58.7 ms: 1.02x faster                                                 |
| sqlalchemy_declarative  | 62.6 ms                                                | 61.5 ms: 1.02x faster                                                 |
| xml_etree_process       | 35.1 ms                                                | 34.5 ms: 1.02x faster                                                 |
| scimark_fft             | 200 ms                                                 | 197 ms: 1.01x faster                                                  |
| spectral_norm           | 72.6 ms                                                | 71.7 ms: 1.01x faster                                                 |
| crypto_pyaes            | 51.7 ms                                                | 51.1 ms: 1.01x faster                                                 |
| genshi_text             | 15.3 ms                                                | 15.1 ms: 1.01x faster                                                 |
| pickle_pure_python      | 201 us                                                 | 198 us: 1.01x faster                                                  |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.12 ms: 1.01x faster                                                 |
| scimark_lu              | 73.3 ms                                                | 72.7 ms: 1.01x faster                                                 |
| async_tree_none         | 286 ms                                                 | 284 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed | 533 ms                                                 | 530 ms: 1.01x faster                                                  |
| sympy_integrate         | 11.5 ms                                                | 11.5 ms: 1.01x faster                                                 |
| pprint_pformat          | 954 ms                                                 | 949 ms: 1.00x faster                                                  |
| django_template         | 21.0 ms                                                | 20.9 ms: 1.00x faster                                                 |
| regex_dna               | 152 ms                                                 | 151 ms: 1.00x faster                                                  |
| thrift                  | 442 us                                                 | 441 us: 1.00x faster                                                  |
| chameleon               | 4.60 ms                                                | 4.59 ms: 1.00x faster                                                 |
| mdp                     | 1.55 sec                                               | 1.55 sec: 1.00x slower                                                |
| sympy_str               | 151 ms                                                 | 152 ms: 1.00x slower                                                  |
| unpickle_pure_python    | 159 us                                                 | 160 us: 1.00x slower                                                  |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| sqlglot_normalize       | 171 ms                                                 | 172 ms: 1.00x slower                                                  |
| docutils                | 1.47 sec                                               | 1.48 sec: 1.00x slower                                                |
| json_loads              | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| deltablue               | 2.81 ms                                                | 2.84 ms: 1.01x slower                                                 |
| async_generators        | 196 ms                                                 | 199 ms: 1.01x slower                                                  |
| generators              | 28.8 ms                                                | 29.1 ms: 1.01x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.85 us: 1.01x slower                                                 |
| json                    | 2.78 ms                                                | 2.82 ms: 1.02x slower                                                 |
| regex_v8                | 16.1 ms                                                | 16.4 ms: 1.02x slower                                                 |
| sympy_expand            | 242 ms                                                 | 247 ms: 1.02x slower                                                  |
| pycparser               | 698 ms                                                 | 711 ms: 1.02x slower                                                  |
| sqlglot_optimize        | 31.1 ms                                                | 31.7 ms: 1.02x slower                                                 |
| raytrace                | 207 ms                                                 | 211 ms: 1.02x slower                                                  |
| logging_simple          | 3.55 us                                                | 3.63 us: 1.02x slower                                                 |
| fannkuch                | 261 ms                                                 | 268 ms: 1.03x slower                                                  |
| hexiom                  | 4.72 ms                                                | 4.84 ms: 1.03x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.16 ms: 1.03x slower                                                 |
| regex_effbot            | 2.63 ms                                                | 2.72 ms: 1.03x slower                                                 |
| logging_format          | 3.78 us                                                | 3.92 us: 1.04x slower                                                 |
| richards                | 32.2 ms                                                | 33.4 ms: 1.04x slower                                                 |
| async_tree_io           | 704 ms                                                 | 734 ms: 1.04x slower                                                  |
| sqlglot_parse           | 959 us                                                 | 1.00 ms: 1.05x slower                                                 |
| meteor_contest          | 73.5 ms                                                | 77.0 ms: 1.05x slower                                                 |
| html5lib                | 34.7 ms                                                | 36.4 ms: 1.05x slower                                                 |
| pickle                  | 7.15 us                                                | 7.59 us: 1.06x slower                                                 |
| go                      | 109 ms                                                 | 117 ms: 1.08x slower                                                  |
| coroutines              | 17.8 ms                                                | 19.3 ms: 1.09x slower                                                 |
| sqlite_synth            | 1.27 us                                                | 1.40 us: 1.10x slower                                                 |
| pyflate                 | 310 ms                                                 | 345 ms: 1.11x slower                                                  |
| async_tree_memoization  | 336 ms                                                 | 381 ms: 1.14x slower                                                  |
| 2to3                    | 161 ms                                                 | 185 ms: 1.14x slower                                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 53.8 ms: 1.16x slower                                                 |
| scimark_sor             | 82.6 ms                                                | 99.0 ms: 1.20x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (6): tornado_http, unpickle, pickle_dict, chaos, pprint_safe_repr, genshi_xml
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, gc_traversal, gunicorn, mypy2, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20220904-3.12.0a0-a0ad63e/bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e.json: mypy


# HPT report

- Reliability score: 51.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
