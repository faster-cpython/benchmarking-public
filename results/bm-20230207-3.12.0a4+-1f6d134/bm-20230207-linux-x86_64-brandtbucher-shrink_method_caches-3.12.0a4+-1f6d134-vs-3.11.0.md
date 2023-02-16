
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_method_caches
- machine: linux-x86_64
- commit hash: 1f6d134
- commit date: 2023-02-07
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.03x faster                                                         |
| chameleon      | 6.38 ms                                                | 6.58 ms: 1.03x slower                                                        |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                       |
| html5lib       | 64.8 ms                                                | 61.3 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                         |
| float          | 76.8 ms                                                | 74.0 ms: 1.04x faster                                                        |
| nbody          | 90.0 ms                                                | 95.8 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                         |
| regex_v8       | 22.2 ms                                                | 21.7 ms: 1.03x faster                                                        |
| regex_dna      | 203 ms                                                 | 207 ms: 1.02x slower                                                         |
| regex_effbot   | 3.46 ms                                                | 3.76 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.47 ms: 1.30x faster                                                        |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                                         |
| json_loads           | 26.1 us                                                | 23.8 us: 1.10x faster                                                        |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                         |
| pickle_pure_python   | 308 us                                                 | 292 us: 1.06x faster                                                         |
| pickle_dict          | 31.2 us                                                | 30.0 us: 1.04x faster                                                        |
| pickle_list          | 4.14 us                                                | 4.05 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                         |
| pickle               | 9.90 us                                                | 9.96 us: 1.01x slower                                                        |
| unpickle_list        | 4.99 us                                                | 5.04 us: 1.01x slower                                                        |
| xml_etree_generate   | 75.9 ms                                                | 77.6 ms: 1.02x slower                                                        |
| unpickle             | 13.3 us                                                | 14.1 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.94 ms: 1.04x slower                                                        |
| python_startup_no_site | 6.04 ms                                                | 6.45 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.3 ms: 1.09x faster                                                        |
| genshi_text     | 21.5 ms                                                | 21.0 ms: 1.02x faster                                                        |
| mako            | 9.83 ms                                                | 9.98 ms: 1.02x slower                                                        |
| django_template | 32.3 ms                                                | 33.2 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 496 ms: 1.78x faster                                                         |
| json_dumps              | 12.4 ms                                                | 9.47 ms: 1.30x faster                                                        |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                         |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                                         |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.11 ms: 1.12x faster                                                        |
| json_loads              | 26.1 us                                                | 23.8 us: 1.10x faster                                                        |
| nqueens                 | 83.8 ms                                                | 76.5 ms: 1.09x faster                                                        |
| deltablue               | 3.66 ms                                                | 3.35 ms: 1.09x faster                                                        |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                         |
| genshi_xml              | 51.4 ms                                                | 47.3 ms: 1.09x faster                                                        |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.08x faster                                                       |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                         |
| sympy_str               | 291 ms                                                 | 274 ms: 1.06x faster                                                         |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                         |
| mdp                     | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                       |
| html5lib                | 64.8 ms                                                | 61.3 ms: 1.06x faster                                                        |
| pickle_pure_python      | 308 us                                                 | 292 us: 1.06x faster                                                         |
| sympy_sum               | 166 ms                                                 | 157 ms: 1.05x faster                                                         |
| hexiom                  | 6.34 ms                                                | 6.02 ms: 1.05x faster                                                        |
| fannkuch                | 384 ms                                                 | 365 ms: 1.05x faster                                                         |
| sympy_integrate         | 21.0 ms                                                | 20.0 ms: 1.05x faster                                                        |
| scimark_fft             | 325 ms                                                 | 312 ms: 1.04x faster                                                         |
| logging_simple          | 6.02 us                                                | 5.78 us: 1.04x faster                                                        |
| chaos                   | 68.7 ms                                                | 65.9 ms: 1.04x faster                                                        |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                         |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                         |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                       |
| float                   | 76.8 ms                                                | 74.0 ms: 1.04x faster                                                        |
| pickle_dict             | 31.2 us                                                | 30.0 us: 1.04x faster                                                        |
| spectral_norm           | 98.1 ms                                                | 94.6 ms: 1.04x faster                                                        |
| richards                | 46.1 ms                                                | 44.6 ms: 1.04x faster                                                        |
| coroutines              | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 1.02 ms: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.0 ms                                                | 65.8 ms: 1.03x faster                                                        |
| pprint_safe_repr        | 706 ms                                                 | 684 ms: 1.03x faster                                                         |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                                       |
| crypto_pyaes            | 75.7 ms                                                | 73.7 ms: 1.03x faster                                                        |
| bench_thread_pool       | 817 us                                                 | 795 us: 1.03x faster                                                         |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.03x faster                                                        |
| regex_v8                | 22.2 ms                                                | 21.7 ms: 1.03x faster                                                        |
| 2to3                    | 259 ms                                                 | 253 ms: 1.03x faster                                                         |
| genshi_text             | 21.5 ms                                                | 21.0 ms: 1.02x faster                                                        |
| pickle_list             | 4.14 us                                                | 4.05 us: 1.02x faster                                                        |
| thrift                  | 760 us                                                 | 745 us: 1.02x faster                                                         |
| pyflate                 | 419 ms                                                 | 412 ms: 1.02x faster                                                         |
| json                    | 4.87 ms                                                | 4.79 ms: 1.02x faster                                                        |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.8 ms: 1.02x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                         |
| sqlglot_optimize        | 52.7 ms                                                | 52.0 ms: 1.01x faster                                                        |
| gunicorn                | 1.12 ms                                                | 1.10 ms: 1.01x faster                                                        |
| raytrace                | 291 ms                                                 | 288 ms: 1.01x faster                                                         |
| unpack_sequence         | 44.5 ns                                                | 44.2 ns: 1.01x faster                                                        |
| pathlib                 | 18.1 ms                                                | 18.0 ms: 1.00x faster                                                        |
| async_generators        | 356 ms                                                 | 354 ms: 1.00x faster                                                         |
| go                      | 140 ms                                                 | 140 ms: 1.00x faster                                                         |
| deepcopy                | 341 us                                                 | 343 us: 1.01x slower                                                         |
| pickle                  | 9.90 us                                                | 9.96 us: 1.01x slower                                                        |
| dulwich_log             | 64.0 ms                                                | 64.5 ms: 1.01x slower                                                        |
| unpickle_list           | 4.99 us                                                | 5.04 us: 1.01x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                                       |
| mako                    | 9.83 ms                                                | 9.98 ms: 1.02x slower                                                        |
| gc_traversal            | 3.82 ms                                                | 3.88 ms: 1.02x slower                                                        |
| regex_dna               | 203 ms                                                 | 207 ms: 1.02x slower                                                         |
| logging_silent          | 98.0 ns                                                | 99.9 ns: 1.02x slower                                                        |
| xml_etree_generate      | 75.9 ms                                                | 77.6 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed | 736 ms                                                 | 753 ms: 1.02x slower                                                         |
| scimark_lu              | 108 ms                                                 | 111 ms: 1.03x slower                                                         |
| django_template         | 32.3 ms                                                | 33.2 ms: 1.03x slower                                                        |
| chameleon               | 6.38 ms                                                | 6.58 ms: 1.03x slower                                                        |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                                        |
| python_startup          | 8.58 ms                                                | 8.94 ms: 1.04x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.74 ms: 1.06x slower                                                        |
| unpickle                | 13.3 us                                                | 14.1 us: 1.06x slower                                                        |
| sqlglot_parse           | 1.36 ms                                                | 1.45 ms: 1.06x slower                                                        |
| async_tree_memoization  | 624 ms                                                 | 664 ms: 1.06x slower                                                         |
| nbody                   | 90.0 ms                                                | 95.8 ms: 1.06x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.45 ms: 1.07x slower                                                        |
| generators              | 73.5 ms                                                | 78.6 ms: 1.07x slower                                                        |
| regex_effbot            | 3.46 ms                                                | 3.76 ms: 1.09x slower                                                        |
| dask                    | 365 ms                                                 | 502 ms: 1.37x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (13): telco, deepcopy_memo, sqlalchemy_declarative, tornado_http, logging_format, meteor_contest, deepcopy_reduce, async_tree_none, coverage, sqlglot_normalize, bench_mp_pool, xml_etree_process, djangocms
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
