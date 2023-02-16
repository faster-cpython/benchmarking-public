
# Results vs. 3.11.0

- fork: python
- ref: e5bd5ad70d9e549eeb80
- machine: linux-x86_64
- commit hash: e5bd5ad
- commit date: 2023-01-13
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                   |
| chameleon      | 6.38 ms                                                | 6.25 ms: 1.02x faster                                                  |
| docutils       | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                 |
| html5lib       | 64.8 ms                                                | 59.7 ms: 1.08x faster                                                  |
| tornado_http   | 96.5 ms                                                | 93.2 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.7 ms: 1.07x faster                                                  |
| pidigits       | 197 ms                                                 | 197 ms: 1.00x slower                                                   |
| nbody          | 90.0 ms                                                | 97.0 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                   |
| regex_v8       | 22.2 ms                                                | 21.6 ms: 1.03x faster                                                  |
| regex_effbot   | 3.46 ms                                                | 3.43 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.35 ms: 1.32x faster                                                  |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                   |
| pickle_pure_python   | 308 us                                                 | 281 us: 1.10x faster                                                   |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.08x faster                                                   |
| json_loads           | 26.1 us                                                | 24.4 us: 1.07x faster                                                  |
| pickle_dict          | 31.2 us                                                | 30.0 us: 1.04x faster                                                  |
| pickle_list          | 4.14 us                                                | 3.99 us: 1.04x faster                                                  |
| unpickle_list        | 4.99 us                                                | 4.88 us: 1.02x faster                                                  |
| xml_etree_process    | 53.7 ms                                                | 53.4 ms: 1.01x faster                                                  |
| pickle               | 9.90 us                                                | 9.86 us: 1.00x faster                                                  |
| xml_etree_generate   | 75.9 ms                                                | 76.3 ms: 1.01x slower                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.54 ms: 1.00x faster                                                  |
| python_startup_no_site | 6.04 ms                                                | 6.11 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.6 ms: 1.10x faster                                                  |
| genshi_text     | 21.5 ms                                                | 20.8 ms: 1.04x faster                                                  |
| django_template | 32.3 ms                                                | 31.9 ms: 1.01x faster                                                  |
| mako            | 9.83 ms                                                | 9.71 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 505 ms: 1.75x faster                                                   |
| json_dumps              | 12.4 ms                                                | 9.35 ms: 1.32x faster                                                  |
| deltablue               | 3.66 ms                                                | 3.17 ms: 1.15x faster                                                  |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                   |
| richards                | 46.1 ms                                                | 41.2 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.15 ms: 1.11x faster                                                  |
| genshi_xml              | 51.4 ms                                                | 46.6 ms: 1.10x faster                                                  |
| pickle_pure_python      | 308 us                                                 | 281 us: 1.10x faster                                                   |
| logging_silent          | 98.0 ns                                                | 89.4 ns: 1.10x faster                                                  |
| html5lib                | 64.8 ms                                                | 59.7 ms: 1.08x faster                                                  |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.08x faster                                                 |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                   |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.08x faster                                                   |
| nqueens                 | 83.8 ms                                                | 77.8 ms: 1.08x faster                                                  |
| float                   | 76.8 ms                                                | 71.7 ms: 1.07x faster                                                  |
| json_loads              | 26.1 us                                                | 24.4 us: 1.07x faster                                                  |
| pprint_safe_repr        | 706 ms                                                 | 663 ms: 1.06x faster                                                   |
| deepcopy_memo           | 35.8 us                                                | 33.7 us: 1.06x faster                                                  |
| logging_simple          | 6.02 us                                                | 5.66 us: 1.06x faster                                                  |
| coroutines              | 26.2 ms                                                | 24.6 ms: 1.06x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                 |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                   |
| scimark_monte_carlo     | 68.0 ms                                                | 64.3 ms: 1.06x faster                                                  |
| aiohttp                 | 1.05 ms                                                | 997 us: 1.05x faster                                                   |
| create_gc_cycles        | 1.52 ms                                                | 1.44 ms: 1.05x faster                                                  |
| hexiom                  | 6.34 ms                                                | 6.03 ms: 1.05x faster                                                  |
| docutils                | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                 |
| bench_thread_pool       | 817 us                                                 | 778 us: 1.05x faster                                                   |
| fannkuch                | 384 ms                                                 | 366 ms: 1.05x faster                                                   |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                  |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                                   |
| pyflate                 | 419 ms                                                 | 401 ms: 1.05x faster                                                   |
| go                      | 140 ms                                                 | 134 ms: 1.04x faster                                                   |
| raytrace                | 291 ms                                                 | 279 ms: 1.04x faster                                                   |
| scimark_fft             | 325 ms                                                 | 312 ms: 1.04x faster                                                   |
| logging_format          | 6.48 us                                                | 6.22 us: 1.04x faster                                                  |
| sqlglot_optimize        | 52.7 ms                                                | 50.6 ms: 1.04x faster                                                  |
| deepcopy                | 341 us                                                 | 329 us: 1.04x faster                                                   |
| spectral_norm           | 98.1 ms                                                | 94.5 ms: 1.04x faster                                                  |
| deepcopy_reduce         | 3.02 us                                                | 2.91 us: 1.04x faster                                                  |
| pickle_dict             | 31.2 us                                                | 30.0 us: 1.04x faster                                                  |
| pickle_list             | 4.14 us                                                | 3.99 us: 1.04x faster                                                  |
| json                    | 4.87 ms                                                | 4.69 ms: 1.04x faster                                                  |
| tornado_http            | 96.5 ms                                                | 93.2 ms: 1.04x faster                                                  |
| genshi_text             | 21.5 ms                                                | 20.8 ms: 1.04x faster                                                  |
| sympy_str               | 291 ms                                                 | 282 ms: 1.03x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                                  |
| telco                   | 6.43 ms                                                | 6.22 ms: 1.03x faster                                                  |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                   |
| dulwich_log             | 64.0 ms                                                | 62.2 ms: 1.03x faster                                                  |
| regex_v8                | 22.2 ms                                                | 21.6 ms: 1.03x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| unpickle_list           | 4.99 us                                                | 4.88 us: 1.02x faster                                                  |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                  |
| chameleon               | 6.38 ms                                                | 6.25 ms: 1.02x faster                                                  |
| coverage                | 99.3 ms                                                | 97.7 ms: 1.02x faster                                                  |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.01x faster                                                   |
| thrift                  | 760 us                                                 | 749 us: 1.01x faster                                                   |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                                   |
| async_generators        | 356 ms                                                 | 351 ms: 1.01x faster                                                   |
| django_template         | 32.3 ms                                                | 31.9 ms: 1.01x faster                                                  |
| mako                    | 9.83 ms                                                | 9.71 ms: 1.01x faster                                                  |
| crypto_pyaes            | 75.7 ms                                                | 74.8 ms: 1.01x faster                                                  |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| chaos                   | 68.7 ms                                                | 68.0 ms: 1.01x faster                                                  |
| regex_effbot            | 3.46 ms                                                | 3.43 ms: 1.01x faster                                                  |
| xml_etree_process       | 53.7 ms                                                | 53.4 ms: 1.01x faster                                                  |
| python_startup          | 8.58 ms                                                | 8.54 ms: 1.00x faster                                                  |
| pickle                  | 9.90 us                                                | 9.86 us: 1.00x faster                                                  |
| pidigits                | 197 ms                                                 | 197 ms: 1.00x slower                                                   |
| xml_etree_generate      | 75.9 ms                                                | 76.3 ms: 1.01x slower                                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.11 ms: 1.01x slower                                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                                 |
| sqlglot_transpile       | 1.65 ms                                                | 1.68 ms: 1.02x slower                                                  |
| mdp                     | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                 |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.03x slower                                                   |
| generators              | 73.5 ms                                                | 75.7 ms: 1.03x slower                                                  |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                                  |
| gc_traversal            | 3.82 ms                                                | 4.05 ms: 1.06x slower                                                  |
| nbody                   | 90.0 ms                                                | 97.0 ms: 1.08x slower                                                  |
| dask                    | 365 ms                                                 | 494 ms: 1.35x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (8): async_tree_memoization, unpickle, djangocms, async_tree_none, regex_dna, bench_mp_pool, unpack_sequence, async_tree_cpu_io_mixed
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230113-3.12.0a4+-e5bd5ad/bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad.json: mypy
