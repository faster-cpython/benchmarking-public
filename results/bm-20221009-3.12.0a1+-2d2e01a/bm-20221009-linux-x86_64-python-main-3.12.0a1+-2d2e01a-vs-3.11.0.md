
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2d2e01a
- commit date: 2022-10-09
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.04x faster                                   |
| chameleon      | 6.47 ms                                                | 6.61 ms: 1.02x slower                                  |
| html5lib       | 64.5 ms                                                | 59.7 ms: 1.08x faster                                  |
| tornado_http   | 96.3 ms                                                | 93.4 ms: 1.03x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.3 ms: 1.07x faster                                  |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| nbody          | 93.1 ms                                                | 94.6 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.60 ms: 1.11x faster                                  |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                   |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.44 ms: 1.33x faster                                  |
| unpickle_pure_python | 228 us                                                 | 204 us: 1.12x faster                                   |
| json_loads           | 26.5 us                                                | 23.8 us: 1.11x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 146 ms: 1.09x faster                                   |
| unpickle             | 13.7 us                                                | 13.0 us: 1.05x faster                                  |
| pickle_pure_python   | 306 us                                                 | 293 us: 1.04x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 101 ms: 1.03x faster                                   |
| pickle_list          | 4.11 us                                                | 4.06 us: 1.01x faster                                  |
| xml_etree_process    | 53.9 ms                                                | 53.7 ms: 1.00x faster                                  |
| xml_etree_generate   | 76.2 ms                                                | 76.6 ms: 1.00x slower                                  |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.02 us: 1.02x slower                                  |
| pickle_dict          | 31.1 us                                                | 31.9 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.38 ms: 1.02x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.06 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 49.1 ms: 1.05x faster                                  |
| mako            | 10.1 ms                                                | 9.84 ms: 1.02x faster                                  |
| genshi_text     | 21.6 ms                                                | 21.8 ms: 1.01x slower                                  |
| django_template | 32.6 ms                                                | 33.3 ms: 1.02x slower                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.44 ms: 1.33x faster                                  |
| scimark_sor             | 118 ms                                                 | 105 ms: 1.13x faster                                   |
| unpickle_pure_python    | 228 us                                                 | 204 us: 1.12x faster                                   |
| json_loads              | 26.5 us                                                | 23.8 us: 1.11x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.60 ms: 1.11x faster                                  |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                  |
| logging_silent          | 101 ns                                                 | 92.7 ns: 1.09x faster                                  |
| pycparser               | 1.18 sec                                               | 1.09 sec: 1.09x faster                                 |
| xml_etree_parse         | 158 ms                                                 | 146 ms: 1.09x faster                                   |
| html5lib                | 64.5 ms                                                | 59.7 ms: 1.08x faster                                  |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                   |
| deltablue               | 3.67 ms                                                | 3.40 ms: 1.08x faster                                  |
| deepcopy_memo           | 37.0 us                                                | 34.3 us: 1.08x faster                                  |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.20 ms: 1.07x faster                                  |
| float                   | 77.2 ms                                                | 72.3 ms: 1.07x faster                                  |
| hexiom                  | 6.37 ms                                                | 6.02 ms: 1.06x faster                                  |
| chaos                   | 69.2 ms                                                | 65.5 ms: 1.06x faster                                  |
| genshi_xml              | 51.8 ms                                                | 49.1 ms: 1.05x faster                                  |
| nqueens                 | 83.4 ms                                                | 79.2 ms: 1.05x faster                                  |
| logging_simple          | 6.03 us                                                | 5.74 us: 1.05x faster                                  |
| unpickle                | 13.7 us                                                | 13.0 us: 1.05x faster                                  |
| json                    | 4.94 ms                                                | 4.72 ms: 1.05x faster                                  |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| 2to3                    | 259 ms                                                 | 248 ms: 1.04x faster                                   |
| raytrace                | 297 ms                                                 | 284 ms: 1.04x faster                                   |
| sqlglot_parse           | 1.40 ms                                                | 1.34 ms: 1.04x faster                                  |
| pickle_pure_python      | 306 us                                                 | 293 us: 1.04x faster                                   |
| telco                   | 6.58 ms                                                | 6.32 ms: 1.04x faster                                  |
| dulwich_log             | 63.7 ms                                                | 61.1 ms: 1.04x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                 |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                   |
| logging_format          | 6.68 us                                                | 6.43 us: 1.04x faster                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.64 ms: 1.04x faster                                  |
| scimark_fft             | 328 ms                                                 | 316 ms: 1.04x faster                                   |
| spectral_norm           | 100 ms                                                 | 96.4 ms: 1.04x faster                                  |
| sympy_str               | 290 ms                                                 | 280 ms: 1.04x faster                                   |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                   |
| sqlglot_optimize        | 53.1 ms                                                | 51.4 ms: 1.03x faster                                  |
| deepcopy                | 342 us                                                 | 331 us: 1.03x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                   |
| tornado_http            | 96.3 ms                                                | 93.4 ms: 1.03x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                  |
| richards                | 45.7 ms                                                | 44.4 ms: 1.03x faster                                  |
| pyflate                 | 418 ms                                                 | 407 ms: 1.03x faster                                   |
| pprint_safe_repr        | 701 ms                                                 | 682 ms: 1.03x faster                                   |
| xml_etree_iterparse     | 104 ms                                                 | 101 ms: 1.03x faster                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 66.3 ms: 1.03x faster                                  |
| thrift                  | 756 us                                                 | 737 us: 1.03x faster                                   |
| pylint                  | 465 ms                                                 | 454 ms: 1.03x faster                                   |
| mako                    | 10.1 ms                                                | 9.84 ms: 1.02x faster                                  |
| coroutines              | 25.5 ms                                                | 25.0 ms: 1.02x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                  |
| sympy_sum               | 167 ms                                                 | 164 ms: 1.02x faster                                   |
| python_startup          | 8.52 ms                                                | 8.38 ms: 1.02x faster                                  |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                   |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                   |
| deepcopy_reduce         | 2.94 us                                                | 2.90 us: 1.01x faster                                  |
| pickle_list             | 4.11 us                                                | 4.06 us: 1.01x faster                                  |
| coverage                | 100 ms                                                 | 98.9 ms: 1.01x faster                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 731 ms: 1.01x faster                                   |
| mdp                     | 2.62 sec                                               | 2.59 sec: 1.01x faster                                 |
| regex_dna               | 204 ms                                                 | 203 ms: 1.00x faster                                   |
| xml_etree_process       | 53.9 ms                                                | 53.7 ms: 1.00x faster                                  |
| generators              | 73.5 ms                                                | 73.8 ms: 1.00x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 76.6 ms: 1.00x slower                                  |
| crypto_pyaes            | 74.7 ms                                                | 75.3 ms: 1.01x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.06 ms: 1.01x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                 |
| genshi_text             | 21.6 ms                                                | 21.8 ms: 1.01x slower                                  |
| nbody                   | 93.1 ms                                                | 94.6 ms: 1.02x slower                                  |
| chameleon               | 6.47 ms                                                | 6.61 ms: 1.02x slower                                  |
| django_template         | 32.6 ms                                                | 33.3 ms: 1.02x slower                                  |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                  |
| unpickle_list           | 4.91 us                                                | 5.02 us: 1.02x slower                                  |
| pickle_dict             | 31.1 us                                                | 31.9 us: 1.03x slower                                  |
| async_tree_memoization  | 627 ms                                                 | 646 ms: 1.03x slower                                   |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 50.2 ns: 1.16x slower                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (2): regex_v8, async_tree_none
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: async_generators, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221009-3.12.0a1+-2d2e01a/bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
