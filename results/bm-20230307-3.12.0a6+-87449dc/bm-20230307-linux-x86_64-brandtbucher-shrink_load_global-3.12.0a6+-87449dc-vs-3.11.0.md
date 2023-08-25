
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_load_global
- machine: linux-x86_64
- commit hash: 87449dc
- commit date: 2023-03-07
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                       |
| chameleon      | 6.47 ms                                                | 6.43 ms: 1.01x faster                                                      |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                     |
| html5lib       | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                      |
| tornado_http   | 96.3 ms                                                | 95.2 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 74.3 ms: 1.04x faster                                                      |
| nbody          | 93.1 ms                                                | 91.6 ms: 1.02x faster                                                      |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.54 ms: 1.13x faster                                                      |
| regex_compile  | 138 ms                                                 | 135 ms: 1.02x faster                                                       |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                      |
| regex_dna      | 204 ms                                                 | 201 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.49 ms: 1.33x faster                                                      |
| unpickle_pure_python | 228 us                                                 | 201 us: 1.13x faster                                                       |
| json_loads           | 26.5 us                                                | 24.2 us: 1.09x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                       |
| pickle_pure_python   | 306 us                                                 | 290 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 99.3 ms: 1.05x faster                                                      |
| pickle_dict          | 31.1 us                                                | 31.2 us: 1.00x slower                                                      |
| pickle_list          | 4.11 us                                                | 4.18 us: 1.02x slower                                                      |
| xml_etree_process    | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                      |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                      |
| unpickle_list        | 4.91 us                                                | 5.13 us: 1.04x slower                                                      |
| xml_etree_generate   | 76.2 ms                                                | 80.9 ms: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.99 ms: 1.06x slower                                                      |
| python_startup_no_site | 6.01 ms                                                | 6.52 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.9 ms: 1.06x faster                                                      |
| mako            | 10.1 ms                                                | 10.1 ms: 1.00x faster                                                      |
| genshi_text     | 21.6 ms                                                | 21.9 ms: 1.02x slower                                                      |
| django_template | 32.6 ms                                                | 33.6 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.9 ms: 2.38x faster                                                      |
| asyncio_tcp             | 922 ms                                                 | 508 ms: 1.81x faster                                                       |
| json_dumps              | 12.6 ms                                                | 9.49 ms: 1.33x faster                                                      |
| mypy2                   | 420 ms                                                 | 334 ms: 1.26x faster                                                       |
| deltablue               | 3.67 ms                                                | 3.23 ms: 1.14x faster                                                      |
| unpickle_pure_python    | 228 us                                                 | 201 us: 1.13x faster                                                       |
| regex_effbot            | 3.99 ms                                                | 3.54 ms: 1.13x faster                                                      |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.10x faster                                                       |
| coroutines              | 25.5 ms                                                | 23.3 ms: 1.10x faster                                                      |
| json_loads              | 26.5 us                                                | 24.2 us: 1.09x faster                                                      |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                      |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                      |
| json                    | 4.94 ms                                                | 4.60 ms: 1.08x faster                                                      |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 34.7 us: 1.07x faster                                                      |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.07x faster                                                     |
| scimark_fft             | 328 ms                                                 | 309 ms: 1.06x faster                                                       |
| coverage                | 100 ms                                                 | 94.4 ms: 1.06x faster                                                      |
| genshi_xml              | 51.8 ms                                                | 48.9 ms: 1.06x faster                                                      |
| mdp                     | 2.62 sec                                               | 2.47 sec: 1.06x faster                                                     |
| fannkuch                | 388 ms                                                 | 367 ms: 1.06x faster                                                       |
| gc_traversal            | 4.02 ms                                                | 3.81 ms: 1.06x faster                                                      |
| pickle_pure_python      | 306 us                                                 | 290 us: 1.06x faster                                                       |
| richards                | 45.7 ms                                                | 43.4 ms: 1.05x faster                                                      |
| html5lib                | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                      |
| spectral_norm           | 100 ms                                                 | 95.2 ms: 1.05x faster                                                      |
| logging_silent          | 101 ns                                                 | 96.4 ns: 1.05x faster                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 99.3 ms: 1.05x faster                                                      |
| float                   | 77.2 ms                                                | 74.3 ms: 1.04x faster                                                      |
| sqlglot_optimize        | 53.1 ms                                                | 51.4 ms: 1.03x faster                                                      |
| bench_thread_pool       | 819 us                                                 | 794 us: 1.03x faster                                                       |
| docutils                | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                     |
| hexiom                  | 6.37 ms                                                | 6.20 ms: 1.03x faster                                                      |
| raytrace                | 297 ms                                                 | 289 ms: 1.03x faster                                                       |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                       |
| crypto_pyaes            | 74.7 ms                                                | 72.8 ms: 1.03x faster                                                      |
| logging_simple          | 6.03 us                                                | 5.88 us: 1.03x faster                                                      |
| regex_compile           | 138 ms                                                 | 135 ms: 1.02x faster                                                       |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                      |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                                     |
| sympy_expand            | 475 ms                                                 | 466 ms: 1.02x faster                                                       |
| scimark_monte_carlo     | 68.1 ms                                                | 66.8 ms: 1.02x faster                                                      |
| chaos                   | 69.2 ms                                                | 68.0 ms: 1.02x faster                                                      |
| nbody                   | 93.1 ms                                                | 91.6 ms: 1.02x faster                                                      |
| logging_format          | 6.68 us                                                | 6.58 us: 1.02x faster                                                      |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                       |
| deepcopy                | 342 us                                                 | 337 us: 1.02x faster                                                       |
| sympy_str               | 290 ms                                                 | 286 ms: 1.01x faster                                                       |
| regex_v8                | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                      |
| telco                   | 6.58 ms                                                | 6.50 ms: 1.01x faster                                                      |
| regex_dna               | 204 ms                                                 | 201 ms: 1.01x faster                                                       |
| sympy_integrate         | 21.0 ms                                                | 20.7 ms: 1.01x faster                                                      |
| tornado_http            | 96.3 ms                                                | 95.2 ms: 1.01x faster                                                      |
| chameleon               | 6.47 ms                                                | 6.43 ms: 1.01x faster                                                      |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.01x faster                                                      |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                       |
| mako                    | 10.1 ms                                                | 10.1 ms: 1.00x faster                                                      |
| pickle_dict             | 31.1 us                                                | 31.2 us: 1.00x slower                                                      |
| sympy_sum               | 167 ms                                                 | 168 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed | 739 ms                                                 | 748 ms: 1.01x slower                                                       |
| scimark_lu              | 110 ms                                                 | 111 ms: 1.01x slower                                                       |
| go                      | 140 ms                                                 | 142 ms: 1.01x slower                                                       |
| pickle_list             | 4.11 us                                                | 4.18 us: 1.02x slower                                                      |
| genshi_text             | 21.6 ms                                                | 21.9 ms: 1.02x slower                                                      |
| django_template         | 32.6 ms                                                | 33.6 ms: 1.03x slower                                                      |
| xml_etree_process       | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                      |
| deepcopy_reduce         | 2.94 us                                                | 3.04 us: 1.03x slower                                                      |
| thrift                  | 756 us                                                 | 784 us: 1.04x slower                                                       |
| sqlglot_transpile       | 1.70 ms                                                | 1.77 ms: 1.04x slower                                                      |
| pickle                  | 10.1 us                                                | 10.5 us: 1.04x slower                                                      |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                                      |
| unpickle_list           | 4.91 us                                                | 5.13 us: 1.04x slower                                                      |
| async_tree_memoization  | 627 ms                                                 | 656 ms: 1.05x slower                                                       |
| unpack_sequence         | 43.1 ns                                                | 45.2 ns: 1.05x slower                                                      |
| sqlglot_parse           | 1.40 ms                                                | 1.47 ms: 1.05x slower                                                      |
| python_startup          | 8.52 ms                                                | 8.99 ms: 1.06x slower                                                      |
| xml_etree_generate      | 76.2 ms                                                | 80.9 ms: 1.06x slower                                                      |
| comprehensions          | 22.4 us                                                | 24.0 us: 1.07x slower                                                      |
| python_startup_no_site  | 6.01 ms                                                | 6.52 ms: 1.09x slower                                                      |
| async_generators        | 368 ms                                                 | 415 ms: 1.13x slower                                                       |
| dask                    | 360 ms                                                 | 512 ms: 1.42x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (12): unpickle, sqlalchemy_declarative, nqueens, async_tree_io, pprint_safe_repr, pyflate, bench_mp_pool, scimark_sparse_mat_mult, dulwich_log, async_tree_none, djangocms, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
