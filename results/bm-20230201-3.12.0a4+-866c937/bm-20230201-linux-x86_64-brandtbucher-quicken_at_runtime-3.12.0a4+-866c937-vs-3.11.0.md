
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 866c937
- commit date: 2023-02-01
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                       |
| chameleon      | 6.47 ms                                                | 6.41 ms: 1.01x faster                                                      |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                     |
| html5lib       | 64.5 ms                                                | 60.1 ms: 1.07x faster                                                      |
| tornado_http   | 96.3 ms                                                | 94.5 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 74.2 ms: 1.04x faster                                                      |
| pidigits       | 198 ms                                                 | 198 ms: 1.00x faster                                                       |
| nbody          | 93.1 ms                                                | 94.9 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                                       |
| regex_effbot   | 3.99 ms                                                | 3.76 ms: 1.06x faster                                                      |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.02x slower                                                      |
| regex_dna      | 204 ms                                                 | 217 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.46 ms: 1.33x faster                                                      |
| unpickle_pure_python | 228 us                                                 | 200 us: 1.14x faster                                                       |
| json_loads           | 26.5 us                                                | 24.3 us: 1.09x faster                                                      |
| pickle_pure_python   | 306 us                                                 | 283 us: 1.08x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                       |
| unpickle             | 13.7 us                                                | 13.3 us: 1.03x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                       |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                      |
| xml_etree_generate   | 76.2 ms                                                | 78.0 ms: 1.02x slower                                                      |
| unpickle_list        | 4.91 us                                                | 5.04 us: 1.03x slower                                                      |
| pickle_list          | 4.11 us                                                | 4.25 us: 1.03x slower                                                      |
| pickle_dict          | 31.1 us                                                | 32.4 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.74 ms: 1.03x slower                                                      |
| python_startup_no_site | 6.01 ms                                                | 6.27 ms: 1.04x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.8 ms: 1.10x faster                                                      |
| genshi_text     | 21.6 ms                                                | 20.7 ms: 1.04x faster                                                      |
| mako            | 10.1 ms                                                | 9.85 ms: 1.02x faster                                                      |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 497 ms: 1.86x faster                                                       |
| json_dumps              | 12.6 ms                                                | 9.46 ms: 1.33x faster                                                      |
| deltablue               | 3.67 ms                                                | 3.18 ms: 1.16x faster                                                      |
| unpickle_pure_python    | 228 us                                                 | 200 us: 1.14x faster                                                       |
| logging_silent          | 101 ns                                                 | 90.6 ns: 1.12x faster                                                      |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.05 ms: 1.11x faster                                                      |
| genshi_xml              | 51.8 ms                                                | 46.8 ms: 1.10x faster                                                      |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                                      |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                                      |
| json_loads              | 26.5 us                                                | 24.3 us: 1.09x faster                                                      |
| richards                | 45.7 ms                                                | 41.9 ms: 1.09x faster                                                      |
| nqueens                 | 83.4 ms                                                | 76.9 ms: 1.08x faster                                                      |
| pickle_pure_python      | 306 us                                                 | 283 us: 1.08x faster                                                       |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 34.3 us: 1.08x faster                                                      |
| sympy_str               | 290 ms                                                 | 269 ms: 1.08x faster                                                       |
| sympy_sum               | 167 ms                                                 | 155 ms: 1.08x faster                                                       |
| html5lib                | 64.5 ms                                                | 60.1 ms: 1.07x faster                                                      |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                       |
| scimark_fft             | 328 ms                                                 | 307 ms: 1.07x faster                                                       |
| hexiom                  | 6.37 ms                                                | 5.96 ms: 1.07x faster                                                      |
| chaos                   | 69.2 ms                                                | 64.8 ms: 1.07x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 19.6 ms: 1.07x faster                                                      |
| regex_effbot            | 3.99 ms                                                | 3.76 ms: 1.06x faster                                                      |
| logging_format          | 6.68 us                                                | 6.32 us: 1.06x faster                                                      |
| json                    | 4.94 ms                                                | 4.69 ms: 1.05x faster                                                      |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                                     |
| gc_traversal            | 4.02 ms                                                | 3.82 ms: 1.05x faster                                                      |
| sympy_expand            | 475 ms                                                 | 452 ms: 1.05x faster                                                       |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                       |
| logging_simple          | 6.03 us                                                | 5.74 us: 1.05x faster                                                      |
| deepcopy                | 342 us                                                 | 326 us: 1.05x faster                                                       |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                     |
| raytrace                | 297 ms                                                 | 283 ms: 1.05x faster                                                       |
| pprint_safe_repr        | 701 ms                                                 | 670 ms: 1.05x faster                                                       |
| bench_thread_pool       | 819 us                                                 | 785 us: 1.04x faster                                                       |
| async_generators        | 368 ms                                                 | 353 ms: 1.04x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.04x faster                                                     |
| float                   | 77.2 ms                                                | 74.2 ms: 1.04x faster                                                      |
| genshi_text             | 21.6 ms                                                | 20.7 ms: 1.04x faster                                                      |
| pyflate                 | 418 ms                                                 | 402 ms: 1.04x faster                                                       |
| scimark_monte_carlo     | 68.1 ms                                                | 65.5 ms: 1.04x faster                                                      |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.04x faster                                                       |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                       |
| spectral_norm           | 100 ms                                                 | 96.9 ms: 1.03x faster                                                      |
| sqlglot_optimize        | 53.1 ms                                                | 51.5 ms: 1.03x faster                                                      |
| unpickle                | 13.7 us                                                | 13.3 us: 1.03x faster                                                      |
| mako                    | 10.1 ms                                                | 9.85 ms: 1.02x faster                                                      |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                     |
| tornado_http            | 96.3 ms                                                | 94.5 ms: 1.02x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                       |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                       |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.02x faster                                                      |
| dulwich_log             | 63.7 ms                                                | 62.8 ms: 1.01x faster                                                      |
| deepcopy_reduce         | 2.94 us                                                | 2.90 us: 1.01x faster                                                      |
| unpack_sequence         | 43.1 ns                                                | 42.6 ns: 1.01x faster                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                       |
| chameleon               | 6.47 ms                                                | 6.41 ms: 1.01x faster                                                      |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                      |
| thrift                  | 756 us                                                 | 750 us: 1.01x faster                                                       |
| crypto_pyaes            | 74.7 ms                                                | 74.2 ms: 1.01x faster                                                      |
| pidigits                | 198 ms                                                 | 198 ms: 1.00x faster                                                       |
| sqlglot_transpile       | 1.70 ms                                                | 1.71 ms: 1.01x slower                                                      |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                      |
| sqlglot_parse           | 1.40 ms                                                | 1.42 ms: 1.02x slower                                                      |
| regex_v8                | 22.0 ms                                                | 22.4 ms: 1.02x slower                                                      |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                                      |
| nbody                   | 93.1 ms                                                | 94.9 ms: 1.02x slower                                                      |
| xml_etree_generate      | 76.2 ms                                                | 78.0 ms: 1.02x slower                                                      |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.02x slower                                                      |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                                     |
| python_startup          | 8.52 ms                                                | 8.74 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed | 739 ms                                                 | 758 ms: 1.03x slower                                                       |
| coroutines              | 25.5 ms                                                | 26.2 ms: 1.03x slower                                                      |
| unpickle_list           | 4.91 us                                                | 5.04 us: 1.03x slower                                                      |
| generators              | 73.5 ms                                                | 76.0 ms: 1.03x slower                                                      |
| pickle_list             | 4.11 us                                                | 4.25 us: 1.03x slower                                                      |
| pickle_dict             | 31.1 us                                                | 32.4 us: 1.04x slower                                                      |
| python_startup_no_site  | 6.01 ms                                                | 6.27 ms: 1.04x slower                                                      |
| async_tree_memoization  | 627 ms                                                 | 661 ms: 1.05x slower                                                       |
| regex_dna               | 204 ms                                                 | 217 ms: 1.06x slower                                                       |
| dask                    | 360 ms                                                 | 501 ms: 1.39x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (6): telco, xml_etree_process, async_tree_none, coverage, bench_mp_pool, djangocms
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230201-3.12.0a4+-866c937/bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
