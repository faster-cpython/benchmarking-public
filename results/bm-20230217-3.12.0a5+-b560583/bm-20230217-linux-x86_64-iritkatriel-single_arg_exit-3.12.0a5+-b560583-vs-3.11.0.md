
# Results vs. 3.11.0

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: b560583
- commit date: 2023-02-17
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 246 ms: 1.05x faster                                                   |
| chameleon      | 6.47 ms                                                | 6.29 ms: 1.03x faster                                                  |
| docutils       | 2.63 sec                                               | 2.54 sec: 1.03x faster                                                 |
| html5lib       | 64.5 ms                                                | 61.7 ms: 1.05x faster                                                  |
| tornado_http   | 96.3 ms                                                | 95.2 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.5 ms: 1.06x faster                                                  |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.28 ms: 1.22x faster                                                  |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                                   |
| regex_v8       | 22.0 ms                                                | 21.3 ms: 1.03x faster                                                  |
| regex_dna      | 204 ms                                                 | 212 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.33 ms: 1.35x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 196 us: 1.16x faster                                                   |
| json_loads           | 26.5 us                                                | 23.5 us: 1.13x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 281 us: 1.09x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                                   |
| unpickle             | 13.7 us                                                | 13.1 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.03x faster                                                   |
| pickle_dict          | 31.1 us                                                | 31.4 us: 1.01x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.18 us: 1.02x slower                                                  |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                  |
| unpickle_list        | 4.91 us                                                | 5.08 us: 1.04x slower                                                  |
| xml_etree_process    | 53.9 ms                                                | 56.2 ms: 1.04x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 80.7 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.97 ms: 1.05x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.50 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.0 ms: 1.08x faster                                                  |
| genshi_text     | 21.6 ms                                                | 20.9 ms: 1.03x faster                                                  |
| mako            | 10.1 ms                                                | 9.89 ms: 1.02x faster                                                  |
| django_template | 32.6 ms                                                | 33.6 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.3 ms: 2.35x faster                                                  |
| asyncio_tcp             | 922 ms                                                 | 501 ms: 1.84x faster                                                   |
| json_dumps              | 12.6 ms                                                | 9.33 ms: 1.35x faster                                                  |
| mypy2                   | 420 ms                                                 | 329 ms: 1.28x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.28 ms: 1.22x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 196 us: 1.16x faster                                                   |
| deltablue               | 3.67 ms                                                | 3.19 ms: 1.15x faster                                                  |
| gc_traversal            | 4.02 ms                                                | 3.53 ms: 1.14x faster                                                  |
| json_loads              | 26.5 us                                                | 23.5 us: 1.13x faster                                                  |
| coroutines              | 25.5 ms                                                | 22.7 ms: 1.12x faster                                                  |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.10x faster                                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.08 ms: 1.10x faster                                                  |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                                  |
| logging_silent          | 101 ns                                                 | 92.1 ns: 1.10x faster                                                  |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                  |
| pickle_pure_python      | 306 us                                                 | 281 us: 1.09x faster                                                   |
| json                    | 4.94 ms                                                | 4.55 ms: 1.09x faster                                                  |
| deepcopy_memo           | 37.0 us                                                | 34.3 us: 1.08x faster                                                  |
| genshi_xml              | 51.8 ms                                                | 48.0 ms: 1.08x faster                                                  |
| richards                | 45.7 ms                                                | 42.4 ms: 1.08x faster                                                  |
| spectral_norm           | 100 ms                                                 | 92.9 ms: 1.08x faster                                                  |
| nqueens                 | 83.4 ms                                                | 77.6 ms: 1.07x faster                                                  |
| scimark_fft             | 328 ms                                                 | 306 ms: 1.07x faster                                                   |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.07x faster                                                 |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                                   |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                                   |
| sympy_str               | 290 ms                                                 | 272 ms: 1.07x faster                                                   |
| float                   | 77.2 ms                                                | 72.5 ms: 1.06x faster                                                  |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                                   |
| logging_format          | 6.68 us                                                | 6.34 us: 1.05x faster                                                  |
| logging_simple          | 6.03 us                                                | 5.73 us: 1.05x faster                                                  |
| sympy_sum               | 167 ms                                                 | 158 ms: 1.05x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 19.9 ms: 1.05x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                                 |
| scimark_monte_carlo     | 68.1 ms                                                | 64.7 ms: 1.05x faster                                                  |
| 2to3                    | 259 ms                                                 | 246 ms: 1.05x faster                                                   |
| raytrace                | 297 ms                                                 | 283 ms: 1.05x faster                                                   |
| telco                   | 6.58 ms                                                | 6.29 ms: 1.05x faster                                                  |
| pprint_safe_repr        | 701 ms                                                 | 670 ms: 1.05x faster                                                   |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                   |
| html5lib                | 64.5 ms                                                | 61.7 ms: 1.05x faster                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 50.8 ms: 1.05x faster                                                  |
| chaos                   | 69.2 ms                                                | 66.2 ms: 1.04x faster                                                  |
| hexiom                  | 6.37 ms                                                | 6.10 ms: 1.04x faster                                                  |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                   |
| go                      | 140 ms                                                 | 134 ms: 1.04x faster                                                   |
| unpack_sequence         | 43.1 ns                                                | 41.3 ns: 1.04x faster                                                  |
| bench_thread_pool       | 819 us                                                 | 785 us: 1.04x faster                                                   |
| unpickle                | 13.7 us                                                | 13.1 us: 1.04x faster                                                  |
| coverage                | 100 ms                                                 | 96.4 ms: 1.04x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.03x faster                                                   |
| regex_v8                | 22.0 ms                                                | 21.3 ms: 1.03x faster                                                  |
| docutils                | 2.63 sec                                               | 2.54 sec: 1.03x faster                                                 |
| genshi_text             | 21.6 ms                                                | 20.9 ms: 1.03x faster                                                  |
| crypto_pyaes            | 74.7 ms                                                | 72.6 ms: 1.03x faster                                                  |
| chameleon               | 6.47 ms                                                | 6.29 ms: 1.03x faster                                                  |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                   |
| pyflate                 | 418 ms                                                 | 408 ms: 1.02x faster                                                   |
| deepcopy                | 342 us                                                 | 335 us: 1.02x faster                                                   |
| mako                    | 10.1 ms                                                | 9.89 ms: 1.02x faster                                                  |
| dulwich_log             | 63.7 ms                                                | 62.6 ms: 1.02x faster                                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.01x faster                                                   |
| tornado_http            | 96.3 ms                                                | 95.2 ms: 1.01x faster                                                  |
| scimark_lu              | 110 ms                                                 | 109 ms: 1.01x faster                                                   |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                  |
| pickle_dict             | 31.1 us                                                | 31.4 us: 1.01x slower                                                  |
| pathlib                 | 18.2 ms                                                | 18.4 ms: 1.01x slower                                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                                  |
| pickle_list             | 4.11 us                                                | 4.18 us: 1.02x slower                                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                 |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                                  |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                                  |
| django_template         | 32.6 ms                                                | 33.6 ms: 1.03x slower                                                  |
| unpickle_list           | 4.91 us                                                | 5.08 us: 1.04x slower                                                  |
| regex_dna               | 204 ms                                                 | 212 ms: 1.04x slower                                                   |
| xml_etree_process       | 53.9 ms                                                | 56.2 ms: 1.04x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.63 us: 1.04x slower                                                  |
| python_startup          | 8.52 ms                                                | 8.97 ms: 1.05x slower                                                  |
| async_tree_memoization  | 627 ms                                                 | 663 ms: 1.06x slower                                                   |
| xml_etree_generate      | 76.2 ms                                                | 80.7 ms: 1.06x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.50 ms: 1.08x slower                                                  |
| async_generators        | 368 ms                                                 | 412 ms: 1.12x slower                                                   |
| dask                    | 360 ms                                                 | 499 ms: 1.39x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (9): deepcopy_reduce, nbody, mdp, bench_mp_pool, thrift, djangocms, async_tree_none, sqlalchemy_imperative, async_tree_cpu_io_mixed
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
