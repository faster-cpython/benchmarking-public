
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 8baef8a
- commit date: 2022-10-02
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 246 ms: 1.05x faster                                   |
| chameleon      | 6.47 ms                                                | 6.38 ms: 1.01x faster                                  |
| html5lib       | 64.5 ms                                                | 59.3 ms: 1.09x faster                                  |
| tornado_http   | 96.3 ms                                                | 92.8 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.0 ms: 1.07x faster                                  |
| pidigits       | 198 ms                                                 | 193 ms: 1.02x faster                                   |
| nbody          | 93.1 ms                                                | 96.2 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.32 ms: 1.20x faster                                  |
| regex_compile  | 138 ms                                                 | 127 ms: 1.09x faster                                   |
| regex_v8       | 22.0 ms                                                | 21.3 ms: 1.03x faster                                  |
| regex_dna      | 204 ms                                                 | 204 ms: 1.00x slower                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.56 ms: 1.32x faster                                  |
| unpickle_pure_python | 228 us                                                 | 201 us: 1.13x faster                                   |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                  |
| pickle_pure_python   | 306 us                                                 | 285 us: 1.07x faster                                   |
| xml_etree_process    | 53.9 ms                                                | 52.9 ms: 1.02x faster                                  |
| pickle_list          | 4.11 us                                                | 4.06 us: 1.01x faster                                  |
| xml_etree_generate   | 76.2 ms                                                | 75.3 ms: 1.01x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 157 ms: 1.01x faster                                   |
| pickle_dict          | 31.1 us                                                | 30.9 us: 1.01x faster                                  |
| unpickle_list        | 4.91 us                                                | 4.96 us: 1.01x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.35 ms: 1.02x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.05 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.1 ms                                                | 9.35 ms: 1.08x faster                                  |
| genshi_xml      | 51.8 ms                                                | 48.4 ms: 1.07x faster                                  |
| genshi_text     | 21.6 ms                                                | 20.7 ms: 1.04x faster                                  |
| django_template | 32.6 ms                                                | 32.4 ms: 1.01x faster                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.56 ms: 1.32x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.32 ms: 1.20x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 201 us: 1.13x faster                                   |
| scimark_sor             | 118 ms                                                 | 105 ms: 1.13x faster                                   |
| deltablue               | 3.67 ms                                                | 3.26 ms: 1.13x faster                                  |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                  |
| deepcopy_memo           | 37.0 us                                                | 33.6 us: 1.10x faster                                  |
| json                    | 4.94 ms                                                | 4.51 ms: 1.10x faster                                  |
| logging_silent          | 101 ns                                                 | 92.6 ns: 1.09x faster                                  |
| regex_compile           | 138 ms                                                 | 127 ms: 1.09x faster                                   |
| html5lib                | 64.5 ms                                                | 59.3 ms: 1.09x faster                                  |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                  |
| spectral_norm           | 100 ms                                                 | 92.3 ms: 1.08x faster                                  |
| mako                    | 10.1 ms                                                | 9.35 ms: 1.08x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.17 ms: 1.08x faster                                  |
| float                   | 77.2 ms                                                | 72.0 ms: 1.07x faster                                  |
| pickle_pure_python      | 306 us                                                 | 285 us: 1.07x faster                                   |
| genshi_xml              | 51.8 ms                                                | 48.4 ms: 1.07x faster                                  |
| mdp                     | 2.62 sec                                               | 2.45 sec: 1.07x faster                                 |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.07x faster                                 |
| coroutines              | 25.5 ms                                                | 23.9 ms: 1.07x faster                                  |
| raytrace                | 297 ms                                                 | 278 ms: 1.07x faster                                   |
| hexiom                  | 6.37 ms                                                | 6.00 ms: 1.06x faster                                  |
| go                      | 140 ms                                                 | 132 ms: 1.06x faster                                   |
| sqlglot_parse           | 1.40 ms                                                | 1.32 ms: 1.06x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                 |
| sqlglot_transpile       | 1.70 ms                                                | 1.61 ms: 1.05x faster                                  |
| deepcopy                | 342 us                                                 | 324 us: 1.05x faster                                   |
| 2to3                    | 259 ms                                                 | 246 ms: 1.05x faster                                   |
| nqueens                 | 83.4 ms                                                | 79.3 ms: 1.05x faster                                  |
| sqlglot_optimize        | 53.1 ms                                                | 50.6 ms: 1.05x faster                                  |
| logging_simple          | 6.03 us                                                | 5.75 us: 1.05x faster                                  |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                   |
| pprint_safe_repr        | 701 ms                                                 | 670 ms: 1.05x faster                                   |
| logging_format          | 6.68 us                                                | 6.39 us: 1.05x faster                                  |
| fannkuch                | 388 ms                                                 | 371 ms: 1.05x faster                                   |
| pyflate                 | 418 ms                                                 | 400 ms: 1.04x faster                                   |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.04x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                   |
| chaos                   | 69.2 ms                                                | 66.4 ms: 1.04x faster                                  |
| genshi_text             | 21.6 ms                                                | 20.7 ms: 1.04x faster                                  |
| telco                   | 6.58 ms                                                | 6.33 ms: 1.04x faster                                  |
| pylint                  | 465 ms                                                 | 447 ms: 1.04x faster                                   |
| dulwich_log             | 63.7 ms                                                | 61.3 ms: 1.04x faster                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 65.6 ms: 1.04x faster                                  |
| tornado_http            | 96.3 ms                                                | 92.8 ms: 1.04x faster                                  |
| scimark_fft             | 328 ms                                                 | 317 ms: 1.04x faster                                   |
| coverage                | 100 ms                                                 | 96.6 ms: 1.04x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.04x faster                                  |
| richards                | 45.7 ms                                                | 44.2 ms: 1.03x faster                                  |
| regex_v8                | 22.0 ms                                                | 21.3 ms: 1.03x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                  |
| sympy_str               | 290 ms                                                 | 281 ms: 1.03x faster                                   |
| async_tree_none         | 526 ms                                                 | 512 ms: 1.03x faster                                   |
| deepcopy_reduce         | 2.94 us                                                | 2.86 us: 1.03x faster                                  |
| crypto_pyaes            | 74.7 ms                                                | 72.8 ms: 1.03x faster                                  |
| pidigits                | 198 ms                                                 | 193 ms: 1.02x faster                                   |
| python_startup          | 8.52 ms                                                | 8.35 ms: 1.02x faster                                  |
| sympy_sum               | 167 ms                                                 | 163 ms: 1.02x faster                                   |
| xml_etree_process       | 53.9 ms                                                | 52.9 ms: 1.02x faster                                  |
| generators              | 73.5 ms                                                | 72.1 ms: 1.02x faster                                  |
| thrift                  | 756 us                                                 | 744 us: 1.02x faster                                   |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.01x faster                                   |
| chameleon               | 6.47 ms                                                | 6.38 ms: 1.01x faster                                  |
| pickle_list             | 4.11 us                                                | 4.06 us: 1.01x faster                                  |
| xml_etree_generate      | 76.2 ms                                                | 75.3 ms: 1.01x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| async_tree_cpu_io_mixed | 739 ms                                                 | 730 ms: 1.01x faster                                   |
| xml_etree_parse         | 158 ms                                                 | 157 ms: 1.01x faster                                   |
| pickle_dict             | 31.1 us                                                | 30.9 us: 1.01x faster                                  |
| django_template         | 32.6 ms                                                | 32.4 ms: 1.01x faster                                  |
| regex_dna               | 204 ms                                                 | 204 ms: 1.00x slower                                   |
| async_tree_io           | 1.30 sec                                               | 1.30 sec: 1.01x slower                                 |
| python_startup_no_site  | 6.01 ms                                                | 6.05 ms: 1.01x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 43.5 ns: 1.01x slower                                  |
| unpickle_list           | 4.91 us                                                | 4.96 us: 1.01x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.57 us: 1.02x slower                                  |
| async_tree_memoization  | 627 ms                                                 | 640 ms: 1.02x slower                                   |
| nbody                   | 93.1 ms                                                | 96.2 ms: 1.03x slower                                  |
| Geometric mean          | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (2): unpickle, pickle
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: async_generators, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221002-3.12.0a1+-8baef8a/bm-20221002-linux-x86_64-python-main-3.12.0a1+-8baef8a.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x
