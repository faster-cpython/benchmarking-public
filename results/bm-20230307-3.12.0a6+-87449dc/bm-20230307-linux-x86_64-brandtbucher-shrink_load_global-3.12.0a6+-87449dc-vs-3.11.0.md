
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_load_global
- machine: linux-x86_64
- commit hash: 87449dc
- commit date: 2023-03-07
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                       |
| chameleon      | 6.38 ms                                                | 6.43 ms: 1.01x slower                                                      |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                     |
| html5lib       | 64.8 ms                                                | 61.3 ms: 1.06x faster                                                      |
| tornado_http   | 96.5 ms                                                | 95.2 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 74.3 ms: 1.03x faster                                                      |
| pidigits       | 197 ms                                                 | 197 ms: 1.00x slower                                                       |
| nbody          | 90.0 ms                                                | 91.6 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                      |
| regex_compile  | 136 ms                                                 | 135 ms: 1.01x faster                                                       |
| regex_dna      | 203 ms                                                 | 201 ms: 1.01x faster                                                       |
| regex_effbot   | 3.46 ms                                                | 3.54 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.49 ms: 1.30x faster                                                      |
| unpickle_pure_python | 227 us                                                 | 201 us: 1.13x faster                                                       |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                       |
| json_loads           | 26.1 us                                                | 24.2 us: 1.08x faster                                                      |
| pickle_pure_python   | 308 us                                                 | 290 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 99.3 ms: 1.05x faster                                                      |
| pickle_dict          | 31.2 us                                                | 31.2 us: 1.00x slower                                                      |
| pickle_list          | 4.14 us                                                | 4.18 us: 1.01x slower                                                      |
| unpickle_list        | 4.99 us                                                | 5.13 us: 1.03x slower                                                      |
| xml_etree_process    | 53.7 ms                                                | 55.6 ms: 1.04x slower                                                      |
| pickle               | 9.90 us                                                | 10.5 us: 1.06x slower                                                      |
| xml_etree_generate   | 75.9 ms                                                | 80.9 ms: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.99 ms: 1.05x slower                                                      |
| python_startup_no_site | 6.04 ms                                                | 6.52 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.9 ms: 1.05x faster                                                      |
| genshi_text     | 21.5 ms                                                | 21.9 ms: 1.02x slower                                                      |
| mako            | 9.83 ms                                                | 10.1 ms: 1.02x slower                                                      |
| django_template | 32.3 ms                                                | 33.6 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.9 ms: 2.38x faster                                                      |
| asyncio_tcp             | 883 ms                                                 | 508 ms: 1.74x faster                                                       |
| json_dumps              | 12.4 ms                                                | 9.49 ms: 1.30x faster                                                      |
| mypy2                   | 420 ms                                                 | 334 ms: 1.26x faster                                                       |
| deltablue               | 3.66 ms                                                | 3.23 ms: 1.13x faster                                                      |
| unpickle_pure_python    | 227 us                                                 | 201 us: 1.13x faster                                                       |
| coroutines              | 26.2 ms                                                | 23.3 ms: 1.12x faster                                                      |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                       |
| json_loads              | 26.1 us                                                | 24.2 us: 1.08x faster                                                      |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                       |
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.07x faster                                                     |
| pickle_pure_python      | 308 us                                                 | 290 us: 1.06x faster                                                       |
| richards                | 46.1 ms                                                | 43.4 ms: 1.06x faster                                                      |
| mdp                     | 2.63 sec                                               | 2.47 sec: 1.06x faster                                                     |
| json                    | 4.87 ms                                                | 4.60 ms: 1.06x faster                                                      |
| html5lib                | 64.8 ms                                                | 61.3 ms: 1.06x faster                                                      |
| scimark_fft             | 325 ms                                                 | 309 ms: 1.05x faster                                                       |
| genshi_xml              | 51.4 ms                                                | 48.9 ms: 1.05x faster                                                      |
| coverage                | 99.3 ms                                                | 94.4 ms: 1.05x faster                                                      |
| xml_etree_iterparse     | 104 ms                                                 | 99.3 ms: 1.05x faster                                                      |
| fannkuch                | 384 ms                                                 | 367 ms: 1.05x faster                                                       |
| crypto_pyaes            | 75.7 ms                                                | 72.8 ms: 1.04x faster                                                      |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                      |
| deepcopy_memo           | 35.8 us                                                | 34.7 us: 1.03x faster                                                      |
| float                   | 76.8 ms                                                | 74.3 ms: 1.03x faster                                                      |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                                      |
| spectral_norm           | 98.1 ms                                                | 95.2 ms: 1.03x faster                                                      |
| bench_thread_pool       | 817 us                                                 | 794 us: 1.03x faster                                                       |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                       |
| sqlglot_optimize        | 52.7 ms                                                | 51.4 ms: 1.03x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                       |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.02x faster                                                      |
| logging_simple          | 6.02 us                                                | 5.88 us: 1.02x faster                                                      |
| regex_v8                | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                      |
| hexiom                  | 6.34 ms                                                | 6.20 ms: 1.02x faster                                                      |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                     |
| sympy_expand            | 475 ms                                                 | 466 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.50 ms: 1.02x faster                                                      |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                                     |
| scimark_monte_carlo     | 68.0 ms                                                | 66.8 ms: 1.02x faster                                                      |
| sympy_str               | 291 ms                                                 | 286 ms: 1.02x faster                                                       |
| logging_silent          | 98.0 ns                                                | 96.4 ns: 1.02x faster                                                      |
| tornado_http            | 96.5 ms                                                | 95.2 ms: 1.01x faster                                                      |
| deepcopy                | 341 us                                                 | 337 us: 1.01x faster                                                       |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                                      |
| regex_compile           | 136 ms                                                 | 135 ms: 1.01x faster                                                       |
| chaos                   | 68.7 ms                                                | 68.0 ms: 1.01x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 20.7 ms: 1.01x faster                                                      |
| regex_dna               | 203 ms                                                 | 201 ms: 1.01x faster                                                       |
| nqueens                 | 83.8 ms                                                | 83.0 ms: 1.01x faster                                                      |
| raytrace                | 291 ms                                                 | 289 ms: 1.01x faster                                                       |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                                       |
| pprint_safe_repr        | 706 ms                                                 | 700 ms: 1.01x faster                                                       |
| async_tree_io           | 1.30 sec                                               | 1.29 sec: 1.01x faster                                                     |
| dulwich_log             | 64.0 ms                                                | 63.7 ms: 1.00x faster                                                      |
| gc_traversal            | 3.82 ms                                                | 3.81 ms: 1.00x faster                                                      |
| pickle_dict             | 31.2 us                                                | 31.2 us: 1.00x slower                                                      |
| pidigits                | 197 ms                                                 | 197 ms: 1.00x slower                                                       |
| meteor_contest          | 104 ms                                                 | 105 ms: 1.01x slower                                                       |
| deepcopy_reduce         | 3.02 us                                                | 3.04 us: 1.01x slower                                                      |
| chameleon               | 6.38 ms                                                | 6.43 ms: 1.01x slower                                                      |
| pickle_list             | 4.14 us                                                | 4.18 us: 1.01x slower                                                      |
| go                      | 140 ms                                                 | 142 ms: 1.01x slower                                                       |
| sympy_sum               | 166 ms                                                 | 168 ms: 1.01x slower                                                       |
| telco                   | 6.43 ms                                                | 6.50 ms: 1.01x slower                                                      |
| unpack_sequence         | 44.5 ns                                                | 45.2 ns: 1.02x slower                                                      |
| logging_format          | 6.48 us                                                | 6.58 us: 1.02x slower                                                      |
| async_tree_cpu_io_mixed | 736 ms                                                 | 748 ms: 1.02x slower                                                       |
| nbody                   | 90.0 ms                                                | 91.6 ms: 1.02x slower                                                      |
| genshi_text             | 21.5 ms                                                | 21.9 ms: 1.02x slower                                                      |
| mako                    | 9.83 ms                                                | 10.1 ms: 1.02x slower                                                      |
| regex_effbot            | 3.46 ms                                                | 3.54 ms: 1.02x slower                                                      |
| unpickle_list           | 4.99 us                                                | 5.13 us: 1.03x slower                                                      |
| scimark_lu              | 108 ms                                                 | 111 ms: 1.03x slower                                                       |
| thrift                  | 760 us                                                 | 784 us: 1.03x slower                                                       |
| xml_etree_process       | 53.7 ms                                                | 55.6 ms: 1.04x slower                                                      |
| django_template         | 32.3 ms                                                | 33.6 ms: 1.04x slower                                                      |
| python_startup          | 8.58 ms                                                | 8.99 ms: 1.05x slower                                                      |
| async_tree_memoization  | 624 ms                                                 | 656 ms: 1.05x slower                                                       |
| pickle                  | 9.90 us                                                | 10.5 us: 1.06x slower                                                      |
| sqlite_synth            | 2.48 us                                                | 2.62 us: 1.06x slower                                                      |
| xml_etree_generate      | 75.9 ms                                                | 80.9 ms: 1.07x slower                                                      |
| sqlglot_transpile       | 1.65 ms                                                | 1.77 ms: 1.07x slower                                                      |
| sqlglot_parse           | 1.36 ms                                                | 1.47 ms: 1.08x slower                                                      |
| python_startup_no_site  | 6.04 ms                                                | 6.52 ms: 1.08x slower                                                      |
| async_generators        | 356 ms                                                 | 415 ms: 1.17x slower                                                       |
| dask                    | 365 ms                                                 | 512 ms: 1.40x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (6): pyflate, bench_mp_pool, djangocms, async_tree_none, sqlalchemy_imperative, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230307-3.12.0a6+-87449dc/bm-20230307-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a6+-87449dc.json: comprehensions
