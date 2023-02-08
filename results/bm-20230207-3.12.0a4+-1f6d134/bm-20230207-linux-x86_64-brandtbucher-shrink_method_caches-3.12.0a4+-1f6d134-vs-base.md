
# Results vs. base

- fork: brandtbucher
- ref: shrink_method_caches
- machine: linux-x86_64
- commit hash: 1f6d134
- commit date: 2023-02-07
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                 | 253 ms: 1.00x faster                                                         |
| chameleon      | 6.27 ms                                                | 6.58 ms: 1.05x slower                                                        |
| docutils       | 2.50 sec                                               | 2.53 sec: 1.01x slower                                                       |
| tornado_http   | 94.6 ms                                                | 96.2 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 72.1 ms                                                | 74.0 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 211 ms                                                 | 207 ms: 1.02x faster                                                         |
| regex_v8       | 21.9 ms                                                | 21.7 ms: 1.01x faster                                                        |
| regex_compile  | 129 ms                                                 | 128 ms: 1.01x faster                                                         |
| regex_effbot   | 3.44 ms                                                | 3.76 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict          | 31.2 us                                                | 30.0 us: 1.04x faster                                                        |
| pickle_list          | 4.16 us                                                | 4.05 us: 1.03x faster                                                        |
| json_loads           | 24.1 us                                                | 23.8 us: 1.01x faster                                                        |
| pickle               | 10.1 us                                                | 9.96 us: 1.01x faster                                                        |
| xml_etree_parse      | 148 ms                                                 | 147 ms: 1.01x faster                                                         |
| xml_etree_generate   | 77.3 ms                                                | 77.6 ms: 1.00x slower                                                        |
| json_dumps           | 9.41 ms                                                | 9.47 ms: 1.01x slower                                                        |
| unpickle_pure_python | 197 us                                                 | 199 us: 1.01x slower                                                         |
| pickle_pure_python   | 286 us                                                 | 292 us: 1.02x slower                                                         |
| unpickle             | 13.0 us                                                | 14.1 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): xml_etree_process, unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.49 ms                                                | 6.45 ms: 1.01x faster                                                        |
| python_startup         | 8.97 ms                                                | 8.94 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 33.5 ms                                                | 33.2 ms: 1.01x faster                                                        |
| genshi_xml      | 46.7 ms                                                | 47.3 ms: 1.01x slower                                                        |
| mako            | 9.72 ms                                                | 9.98 ms: 1.03x slower                                                        |
| genshi_text     | 20.4 ms                                                | 21.0 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                     | 2.73 sec                                               | 2.48 sec: 1.10x faster                                                       |
| pycparser               | 1.15 sec                                               | 1.09 sec: 1.05x faster                                                       |
| thrift                  | 777 us                                                 | 745 us: 1.04x faster                                                         |
| pickle_dict             | 31.2 us                                                | 30.0 us: 1.04x faster                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 65.8 ms: 1.03x faster                                                        |
| nqueens                 | 78.8 ms                                                | 76.5 ms: 1.03x faster                                                        |
| pickle_list             | 4.16 us                                                | 4.05 us: 1.03x faster                                                        |
| regex_dna               | 211 ms                                                 | 207 ms: 1.02x faster                                                         |
| spectral_norm           | 96.5 ms                                                | 94.6 ms: 1.02x faster                                                        |
| pprint_safe_repr        | 695 ms                                                 | 684 ms: 1.02x faster                                                         |
| json_loads              | 24.1 us                                                | 23.8 us: 1.01x faster                                                        |
| unpack_sequence         | 44.7 ns                                                | 44.2 ns: 1.01x faster                                                        |
| regex_v8                | 21.9 ms                                                | 21.7 ms: 1.01x faster                                                        |
| crypto_pyaes            | 74.4 ms                                                | 73.7 ms: 1.01x faster                                                        |
| pickle                  | 10.1 us                                                | 9.96 us: 1.01x faster                                                        |
| async_tree_cpu_io_mixed | 760 ms                                                 | 753 ms: 1.01x faster                                                         |
| pprint_pformat          | 1.42 sec                                               | 1.40 sec: 1.01x faster                                                       |
| django_template         | 33.5 ms                                                | 33.2 ms: 1.01x faster                                                        |
| python_startup_no_site  | 6.49 ms                                                | 6.45 ms: 1.01x faster                                                        |
| regex_compile           | 129 ms                                                 | 128 ms: 1.01x faster                                                         |
| xml_etree_parse         | 148 ms                                                 | 147 ms: 1.01x faster                                                         |
| async_generators        | 356 ms                                                 | 354 ms: 1.00x faster                                                         |
| python_startup          | 8.97 ms                                                | 8.94 ms: 1.00x faster                                                        |
| 2to3                    | 254 ms                                                 | 253 ms: 1.00x faster                                                         |
| xml_etree_generate      | 77.3 ms                                                | 77.6 ms: 1.00x slower                                                        |
| asyncio_tcp             | 494 ms                                                 | 496 ms: 1.00x slower                                                         |
| hexiom                  | 5.99 ms                                                | 6.02 ms: 1.01x slower                                                        |
| create_gc_cycles        | 1.47 ms                                                | 1.48 ms: 1.01x slower                                                        |
| chaos                   | 65.5 ms                                                | 65.9 ms: 1.01x slower                                                        |
| json_dumps              | 9.41 ms                                                | 9.47 ms: 1.01x slower                                                        |
| mypy2                   | 331 ms                                                 | 333 ms: 1.01x slower                                                         |
| unpickle_pure_python    | 197 us                                                 | 199 us: 1.01x slower                                                         |
| logging_format          | 6.39 us                                                | 6.46 us: 1.01x slower                                                        |
| fannkuch                | 362 ms                                                 | 365 ms: 1.01x slower                                                         |
| docutils                | 2.50 sec                                               | 2.53 sec: 1.01x slower                                                       |
| scimark_fft             | 308 ms                                                 | 312 ms: 1.01x slower                                                         |
| sympy_sum               | 156 ms                                                 | 157 ms: 1.01x slower                                                         |
| aiohttp                 | 1.00 ms                                                | 1.02 ms: 1.01x slower                                                        |
| pathlib                 | 17.7 ms                                                | 18.0 ms: 1.01x slower                                                        |
| deepcopy_reduce         | 2.97 us                                                | 3.01 us: 1.01x slower                                                        |
| sympy_integrate         | 19.7 ms                                                | 20.0 ms: 1.01x slower                                                        |
| genshi_xml              | 46.7 ms                                                | 47.3 ms: 1.01x slower                                                        |
| sympy_str               | 270 ms                                                 | 274 ms: 1.01x slower                                                         |
| go                      | 138 ms                                                 | 140 ms: 1.02x slower                                                         |
| deltablue               | 3.30 ms                                                | 3.35 ms: 1.02x slower                                                        |
| tornado_http            | 94.6 ms                                                | 96.2 ms: 1.02x slower                                                        |
| bench_thread_pool       | 781 us                                                 | 795 us: 1.02x slower                                                         |
| sqlglot_transpile       | 1.71 ms                                                | 1.74 ms: 1.02x slower                                                        |
| gunicorn                | 1.08 ms                                                | 1.10 ms: 1.02x slower                                                        |
| gc_traversal            | 3.80 ms                                                | 3.88 ms: 1.02x slower                                                        |
| sqlglot_parse           | 1.42 ms                                                | 1.45 ms: 1.02x slower                                                        |
| pickle_pure_python      | 286 us                                                 | 292 us: 1.02x slower                                                         |
| dulwich_log             | 63.1 ms                                                | 64.5 ms: 1.02x slower                                                        |
| generators              | 76.8 ms                                                | 78.6 ms: 1.02x slower                                                        |
| sqlglot_optimize        | 50.8 ms                                                | 52.0 ms: 1.02x slower                                                        |
| scimark_lu              | 108 ms                                                 | 111 ms: 1.02x slower                                                         |
| scimark_sparse_mat_mult | 4.01 ms                                                | 4.11 ms: 1.02x slower                                                        |
| float                   | 72.1 ms                                                | 74.0 ms: 1.03x slower                                                        |
| mako                    | 9.72 ms                                                | 9.98 ms: 1.03x slower                                                        |
| sqlglot_normalize       | 104 ms                                                 | 108 ms: 1.03x slower                                                         |
| pyflate                 | 399 ms                                                 | 412 ms: 1.03x slower                                                         |
| genshi_text             | 20.4 ms                                                | 21.0 ms: 1.03x slower                                                        |
| json                    | 4.62 ms                                                | 4.79 ms: 1.04x slower                                                        |
| coverage                | 95.3 ms                                                | 99.2 ms: 1.04x slower                                                        |
| deepcopy_memo           | 34.2 us                                                | 35.7 us: 1.04x slower                                                        |
| deepcopy                | 327 us                                                 | 343 us: 1.05x slower                                                         |
| chameleon               | 6.27 ms                                                | 6.58 ms: 1.05x slower                                                        |
| logging_silent          | 93.8 ns                                                | 99.9 ns: 1.07x slower                                                        |
| richards                | 41.8 ms                                                | 44.6 ms: 1.07x slower                                                        |
| unpickle                | 13.0 us                                                | 14.1 us: 1.08x slower                                                        |
| regex_effbot            | 3.44 ms                                                | 3.76 ms: 1.09x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (22): sqlalchemy_imperative, scimark_sor, dask, async_tree_io, meteor_contest, async_tree_memoization, async_tree_none, logging_simple, xml_etree_process, sqlite_synth, bench_mp_pool, sympy_expand, pidigits, unpickle_list, xml_etree_iterparse, telco, coroutines, sqlalchemy_declarative, nbody, raytrace, html5lib, djangocms
