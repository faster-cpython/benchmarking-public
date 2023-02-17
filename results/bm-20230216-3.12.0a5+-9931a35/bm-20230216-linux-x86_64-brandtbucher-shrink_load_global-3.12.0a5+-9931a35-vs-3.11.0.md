
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_load_global
- machine: linux-x86_64
- commit hash: 9931a35
- commit date: 2023-02-16
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 246 ms: 1.06x faster                                                       |
| chameleon      | 6.38 ms                                                | 6.52 ms: 1.02x slower                                                      |
| docutils       | 2.60 sec                                               | 2.54 sec: 1.02x faster                                                     |
| html5lib       | 64.8 ms                                                | 60.9 ms: 1.06x faster                                                      |
| tornado_http   | 96.5 ms                                                | 95.2 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.9 ms: 1.05x faster                                                      |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                       |
| nbody          | 90.0 ms                                                | 94.4 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.05x faster                                                       |
| regex_v8       | 22.2 ms                                                | 21.7 ms: 1.02x faster                                                      |
| regex_dna      | 203 ms                                                 | 206 ms: 1.01x slower                                                       |
| regex_effbot   | 3.46 ms                                                | 3.70 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.64 ms: 1.28x faster                                                      |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                       |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                       |
| pickle_pure_python   | 308 us                                                 | 283 us: 1.09x faster                                                       |
| json_loads           | 26.1 us                                                | 24.2 us: 1.08x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                       |
| unpickle_list        | 4.99 us                                                | 5.06 us: 1.02x slower                                                      |
| pickle_dict          | 31.2 us                                                | 31.7 us: 1.02x slower                                                      |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                      |
| pickle_list          | 4.14 us                                                | 4.26 us: 1.03x slower                                                      |
| xml_etree_process    | 53.7 ms                                                | 56.3 ms: 1.05x slower                                                      |
| xml_etree_generate   | 75.9 ms                                                | 81.9 ms: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.96 ms: 1.05x slower                                                      |
| python_startup_no_site | 6.04 ms                                                | 6.49 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.4 ms: 1.06x faster                                                      |
| genshi_text     | 21.5 ms                                                | 21.3 ms: 1.01x faster                                                      |
| mako            | 9.83 ms                                                | 10.0 ms: 1.02x slower                                                      |
| django_template | 32.3 ms                                                | 33.1 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230216-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-9931a35 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.6 ms: 2.40x faster                                                      |
| asyncio_tcp             | 883 ms                                                 | 504 ms: 1.75x faster                                                       |
| json_dumps              | 12.4 ms                                                | 9.64 ms: 1.28x faster                                                      |
| mypy2                   | 420 ms                                                 | 330 ms: 1.27x faster                                                       |
| coroutines              | 26.2 ms                                                | 22.6 ms: 1.16x faster                                                      |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                       |
| deltablue               | 3.66 ms                                                | 3.20 ms: 1.14x faster                                                      |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.08 ms: 1.12x faster                                                      |
| richards                | 46.1 ms                                                | 42.2 ms: 1.09x faster                                                      |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                       |
| pickle_pure_python      | 308 us                                                 | 283 us: 1.09x faster                                                       |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.09x faster                                                     |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                       |
| sympy_str               | 291 ms                                                 | 271 ms: 1.08x faster                                                       |
| json_loads              | 26.1 us                                                | 24.2 us: 1.08x faster                                                      |
| html5lib                | 64.8 ms                                                | 60.9 ms: 1.06x faster                                                      |
| unpack_sequence         | 44.5 ns                                                | 41.8 ns: 1.06x faster                                                      |
| genshi_xml              | 51.4 ms                                                | 48.4 ms: 1.06x faster                                                      |
| json                    | 4.87 ms                                                | 4.60 ms: 1.06x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 19.9 ms: 1.06x faster                                                      |
| 2to3                    | 259 ms                                                 | 246 ms: 1.06x faster                                                       |
| regex_compile           | 136 ms                                                 | 129 ms: 1.05x faster                                                       |
| sympy_sum               | 166 ms                                                 | 157 ms: 1.05x faster                                                       |
| float                   | 76.8 ms                                                | 72.9 ms: 1.05x faster                                                      |
| scimark_fft             | 325 ms                                                 | 309 ms: 1.05x faster                                                       |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                      |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                       |
| gc_traversal            | 3.82 ms                                                | 3.66 ms: 1.04x faster                                                      |
| pyflate                 | 419 ms                                                 | 401 ms: 1.04x faster                                                       |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                                      |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                     |
| nqueens                 | 83.8 ms                                                | 80.5 ms: 1.04x faster                                                      |
| pprint_safe_repr        | 706 ms                                                 | 681 ms: 1.04x faster                                                       |
| hexiom                  | 6.34 ms                                                | 6.12 ms: 1.04x faster                                                      |
| fannkuch                | 384 ms                                                 | 371 ms: 1.04x faster                                                       |
| logging_simple          | 6.02 us                                                | 5.82 us: 1.03x faster                                                      |
| spectral_norm           | 98.1 ms                                                | 94.9 ms: 1.03x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                       |
| sqlglot_optimize        | 52.7 ms                                                | 51.1 ms: 1.03x faster                                                      |
| bench_thread_pool       | 817 us                                                 | 792 us: 1.03x faster                                                       |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                       |
| scimark_monte_carlo     | 68.0 ms                                                | 66.0 ms: 1.03x faster                                                      |
| chaos                   | 68.7 ms                                                | 66.7 ms: 1.03x faster                                                      |
| crypto_pyaes            | 75.7 ms                                                | 73.6 ms: 1.03x faster                                                      |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                      |
| deepcopy_memo           | 35.8 us                                                | 34.9 us: 1.03x faster                                                      |
| coverage                | 99.3 ms                                                | 96.8 ms: 1.03x faster                                                      |
| regex_v8                | 22.2 ms                                                | 21.7 ms: 1.02x faster                                                      |
| logging_silent          | 98.0 ns                                                | 95.8 ns: 1.02x faster                                                      |
| docutils                | 2.60 sec                                               | 2.54 sec: 1.02x faster                                                     |
| dulwich_log             | 64.0 ms                                                | 62.9 ms: 1.02x faster                                                      |
| logging_format          | 6.48 us                                                | 6.37 us: 1.02x faster                                                      |
| raytrace                | 291 ms                                                 | 287 ms: 1.02x faster                                                       |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                       |
| tornado_http            | 96.5 ms                                                | 95.2 ms: 1.01x faster                                                      |
| deepcopy_reduce         | 3.02 us                                                | 2.98 us: 1.01x faster                                                      |
| deepcopy                | 341 us                                                 | 337 us: 1.01x faster                                                       |
| genshi_text             | 21.5 ms                                                | 21.3 ms: 1.01x faster                                                      |
| pathlib                 | 18.1 ms                                                | 18.0 ms: 1.01x faster                                                      |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                     |
| thrift                  | 760 us                                                 | 766 us: 1.01x slower                                                       |
| scimark_lu              | 108 ms                                                 | 109 ms: 1.01x slower                                                       |
| regex_dna               | 203 ms                                                 | 206 ms: 1.01x slower                                                       |
| unpickle_list           | 4.99 us                                                | 5.06 us: 1.02x slower                                                      |
| pickle_dict             | 31.2 us                                                | 31.7 us: 1.02x slower                                                      |
| mdp                     | 2.63 sec                                               | 2.68 sec: 1.02x slower                                                     |
| mako                    | 9.83 ms                                                | 10.0 ms: 1.02x slower                                                      |
| chameleon               | 6.38 ms                                                | 6.52 ms: 1.02x slower                                                      |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                      |
| django_template         | 32.3 ms                                                | 33.1 ms: 1.03x slower                                                      |
| pickle_list             | 4.14 us                                                | 4.26 us: 1.03x slower                                                      |
| async_tree_memoization  | 624 ms                                                 | 644 ms: 1.03x slower                                                       |
| python_startup          | 8.58 ms                                                | 8.96 ms: 1.05x slower                                                      |
| nbody                   | 90.0 ms                                                | 94.4 ms: 1.05x slower                                                      |
| xml_etree_process       | 53.7 ms                                                | 56.3 ms: 1.05x slower                                                      |
| sqlglot_transpile       | 1.65 ms                                                | 1.73 ms: 1.05x slower                                                      |
| sqlglot_parse           | 1.36 ms                                                | 1.44 ms: 1.06x slower                                                      |
| sqlite_synth            | 2.48 us                                                | 2.63 us: 1.06x slower                                                      |
| regex_effbot            | 3.46 ms                                                | 3.70 ms: 1.07x slower                                                      |
| python_startup_no_site  | 6.04 ms                                                | 6.49 ms: 1.08x slower                                                      |
| xml_etree_generate      | 75.9 ms                                                | 81.9 ms: 1.08x slower                                                      |
| async_generators        | 356 ms                                                 | 412 ms: 1.16x slower                                                       |
| dask                    | 365 ms                                                 | 500 ms: 1.37x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (9): telco, meteor_contest, async_tree_none, sqlalchemy_declarative, bench_mp_pool, sqlalchemy_imperative, async_tree_cpu_io_mixed, djangocms, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
