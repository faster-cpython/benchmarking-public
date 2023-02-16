
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: dec1ab0
- commit date: 2023-02-07
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 254 ms: 1.02x faster                                   |
| chameleon      | 6.38 ms                                                | 6.27 ms: 1.02x faster                                  |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                 |
| html5lib       | 64.8 ms                                                | 60.8 ms: 1.07x faster                                  |
| tornado_http   | 96.5 ms                                                | 94.6 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.1 ms: 1.06x faster                                  |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                   |
| nbody          | 90.0 ms                                                | 95.4 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                   |
| regex_v8       | 22.2 ms                                                | 21.9 ms: 1.01x faster                                  |
| regex_dna      | 203 ms                                                 | 211 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.41 ms: 1.31x faster                                  |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                   |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                   |
| json_loads           | 26.1 us                                                | 24.1 us: 1.08x faster                                  |
| pickle_pure_python   | 308 us                                                 | 286 us: 1.08x faster                                   |
| unpickle             | 13.3 us                                                | 13.0 us: 1.02x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| pickle_dict          | 31.2 us                                                | 31.2 us: 1.00x slower                                  |
| xml_etree_process    | 53.7 ms                                                | 53.9 ms: 1.00x slower                                  |
| pickle_list          | 4.14 us                                                | 4.16 us: 1.00x slower                                  |
| unpickle_list        | 4.99 us                                                | 5.04 us: 1.01x slower                                  |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                  |
| xml_etree_generate   | 75.9 ms                                                | 77.3 ms: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.97 ms: 1.05x slower                                  |
| python_startup_no_site | 6.04 ms                                                | 6.49 ms: 1.07x slower                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.7 ms: 1.10x faster                                  |
| genshi_text     | 21.5 ms                                                | 20.4 ms: 1.06x faster                                  |
| mako            | 9.83 ms                                                | 9.72 ms: 1.01x faster                                  |
| django_template | 32.3 ms                                                | 33.5 ms: 1.04x slower                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-main-3.12.0a4+-dec1ab0 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 494 ms: 1.79x faster                                   |
| json_dumps              | 12.4 ms                                                | 9.41 ms: 1.31x faster                                  |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                   |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                   |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.01 ms: 1.14x faster                                  |
| deltablue               | 3.66 ms                                                | 3.30 ms: 1.11x faster                                  |
| richards                | 46.1 ms                                                | 41.8 ms: 1.11x faster                                  |
| genshi_xml              | 51.4 ms                                                | 46.7 ms: 1.10x faster                                  |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                   |
| json_loads              | 26.1 us                                                | 24.1 us: 1.08x faster                                  |
| pickle_pure_python      | 308 us                                                 | 286 us: 1.08x faster                                   |
| sympy_str               | 291 ms                                                 | 270 ms: 1.08x faster                                   |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                   |
| html5lib                | 64.8 ms                                                | 60.8 ms: 1.07x faster                                  |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.07x faster                                   |
| float                   | 76.8 ms                                                | 72.1 ms: 1.06x faster                                  |
| fannkuch                | 384 ms                                                 | 362 ms: 1.06x faster                                   |
| nqueens                 | 83.8 ms                                                | 78.8 ms: 1.06x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                  |
| hexiom                  | 6.34 ms                                                | 5.99 ms: 1.06x faster                                  |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                   |
| scimark_fft             | 325 ms                                                 | 308 ms: 1.06x faster                                   |
| genshi_text             | 21.5 ms                                                | 20.4 ms: 1.06x faster                                  |
| json                    | 4.87 ms                                                | 4.62 ms: 1.05x faster                                  |
| chaos                   | 68.7 ms                                                | 65.5 ms: 1.05x faster                                  |
| pyflate                 | 419 ms                                                 | 399 ms: 1.05x faster                                   |
| deepcopy_memo           | 35.8 us                                                | 34.2 us: 1.05x faster                                  |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                  |
| bench_thread_pool       | 817 us                                                 | 781 us: 1.05x faster                                   |
| logging_silent          | 98.0 ns                                                | 93.8 ns: 1.05x faster                                  |
| deepcopy                | 341 us                                                 | 327 us: 1.04x faster                                   |
| coverage                | 99.3 ms                                                | 95.3 ms: 1.04x faster                                  |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                   |
| logging_simple          | 6.02 us                                                | 5.78 us: 1.04x faster                                  |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                 |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                   |
| coroutines              | 26.2 ms                                                | 25.2 ms: 1.04x faster                                  |
| sqlglot_optimize        | 52.7 ms                                                | 50.8 ms: 1.04x faster                                  |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                  |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.03x faster                                 |
| pycparser               | 1.19 sec                                               | 1.15 sec: 1.03x faster                                 |
| 2to3                    | 259 ms                                                 | 254 ms: 1.02x faster                                   |
| tornado_http            | 96.5 ms                                                | 94.6 ms: 1.02x faster                                  |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                   |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                  |
| chameleon               | 6.38 ms                                                | 6.27 ms: 1.02x faster                                  |
| crypto_pyaes            | 75.7 ms                                                | 74.4 ms: 1.02x faster                                  |
| raytrace                | 291 ms                                                 | 287 ms: 1.02x faster                                   |
| unpickle                | 13.3 us                                                | 13.0 us: 1.02x faster                                  |
| spectral_norm           | 98.1 ms                                                | 96.5 ms: 1.02x faster                                  |
| deepcopy_reduce         | 3.02 us                                                | 2.97 us: 1.02x faster                                  |
| pprint_safe_repr        | 706 ms                                                 | 695 ms: 1.02x faster                                   |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| dulwich_log             | 64.0 ms                                                | 63.1 ms: 1.01x faster                                  |
| regex_v8                | 22.2 ms                                                | 21.9 ms: 1.01x faster                                  |
| logging_format          | 6.48 us                                                | 6.39 us: 1.01x faster                                  |
| mako                    | 9.83 ms                                                | 9.72 ms: 1.01x faster                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                   |
| telco                   | 6.43 ms                                                | 6.38 ms: 1.01x faster                                  |
| gc_traversal            | 3.82 ms                                                | 3.80 ms: 1.01x faster                                  |
| pickle_dict             | 31.2 us                                                | 31.2 us: 1.00x slower                                  |
| xml_etree_process       | 53.7 ms                                                | 53.9 ms: 1.00x slower                                  |
| pickle_list             | 4.14 us                                                | 4.16 us: 1.00x slower                                  |
| unpack_sequence         | 44.5 ns                                                | 44.7 ns: 1.01x slower                                  |
| unpickle_list           | 4.99 us                                                | 5.04 us: 1.01x slower                                  |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                 |
| xml_etree_generate      | 75.9 ms                                                | 77.3 ms: 1.02x slower                                  |
| thrift                  | 760 us                                                 | 777 us: 1.02x slower                                   |
| async_tree_cpu_io_mixed | 736 ms                                                 | 760 ms: 1.03x slower                                   |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.03x slower                                  |
| django_template         | 32.3 ms                                                | 33.5 ms: 1.04x slower                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.42 ms: 1.04x slower                                  |
| regex_dna               | 203 ms                                                 | 211 ms: 1.04x slower                                   |
| mdp                     | 2.63 sec                                               | 2.73 sec: 1.04x slower                                 |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                  |
| generators              | 73.5 ms                                                | 76.8 ms: 1.04x slower                                  |
| python_startup          | 8.58 ms                                                | 8.97 ms: 1.05x slower                                  |
| nbody                   | 90.0 ms                                                | 95.4 ms: 1.06x slower                                  |
| async_tree_memoization  | 624 ms                                                 | 665 ms: 1.07x slower                                   |
| python_startup_no_site  | 6.04 ms                                                | 6.49 ms: 1.07x slower                                  |
| dask                    | 365 ms                                                 | 504 ms: 1.38x slower                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (9): djangocms, regex_effbot, async_tree_none, meteor_contest, sqlalchemy_imperative, async_generators, bench_mp_pool, scimark_lu, scimark_monte_carlo
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
