
# Results vs. 3.11.0

- fork: python
- ref: e5bd5ad70d9e549eeb80
- machine: linux-x86_64
- commit hash: e5bd5ad
- commit date: 2023-01-13
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 251 ms: 1.02x faster                                                   |
| chameleon      | 6.41 ms                                                | 6.25 ms: 1.03x faster                                                  |
| docutils       | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                 |
| html5lib       | 63.2 ms                                                | 59.7 ms: 1.06x faster                                                  |
| tornado_http   | 96.6 ms                                                | 93.2 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 71.7 ms: 1.06x faster                                                  |
| nbody          | 95.0 ms                                                | 97.0 ms: 1.02x slower                                                  |
| pidigits       | 199 ms                                                 | 197 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.05x faster                                                   |
| regex_effbot   | 3.36 ms                                                | 3.43 ms: 1.02x slower                                                  |
| regex_v8       | 22.3 ms                                                | 21.6 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.35 ms: 1.35x faster                                                  |
| json_loads           | 26.2 us                                                | 24.4 us: 1.07x faster                                                  |
| pickle               | 9.79 us                                                | 9.86 us: 1.01x slower                                                  |
| pickle_dict          | 31.4 us                                                | 30.0 us: 1.05x faster                                                  |
| pickle_list          | 4.17 us                                                | 3.99 us: 1.05x faster                                                  |
| pickle_pure_python   | 304 us                                                 | 281 us: 1.08x faster                                                   |
| unpickle_list        | 4.95 us                                                | 4.88 us: 1.02x faster                                                  |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                   |
| xml_etree_iterparse  | 103 ms                                                 | 107 ms: 1.04x slower                                                   |
| xml_etree_process    | 53.8 ms                                                | 53.4 ms: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (2): unpickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.54 ms: 1.02x slower                                                  |
| python_startup_no_site | 5.96 ms                                                | 6.11 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 32.5 ms                                                | 31.9 ms: 1.02x faster                                                  |
| genshi_text     | 22.1 ms                                                | 20.8 ms: 1.06x faster                                                  |
| genshi_xml      | 52.1 ms                                                | 46.6 ms: 1.12x faster                                                  |
| mako            | 9.85 ms                                                | 9.71 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 251 ms: 1.02x faster                                                   |
| aiohttp                 | 1.05 ms                                                | 997 us: 1.05x faster                                                   |
| async_generators        | 359 ms                                                 | 351 ms: 1.02x faster                                                   |
| async_tree_none         | 529 ms                                                 | 524 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed | 752 ms                                                 | 737 ms: 1.02x faster                                                   |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                 |
| chameleon               | 6.41 ms                                                | 6.25 ms: 1.03x faster                                                  |
| chaos                   | 68.6 ms                                                | 68.0 ms: 1.01x faster                                                  |
| bench_thread_pool       | 810 us                                                 | 778 us: 1.04x faster                                                   |
| coroutines              | 26.1 ms                                                | 24.6 ms: 1.06x faster                                                  |
| coverage                | 101 ms                                                 | 97.7 ms: 1.03x faster                                                  |
| crypto_pyaes            | 73.9 ms                                                | 74.8 ms: 1.01x slower                                                  |
| deepcopy                | 344 us                                                 | 329 us: 1.05x faster                                                   |
| deepcopy_reduce         | 2.97 us                                                | 2.91 us: 1.02x faster                                                  |
| deepcopy_memo           | 36.4 us                                                | 33.7 us: 1.08x faster                                                  |
| deltablue               | 3.64 ms                                                | 3.17 ms: 1.15x faster                                                  |
| django_template         | 32.5 ms                                                | 31.9 ms: 1.02x faster                                                  |
| docutils                | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                 |
| dulwich_log             | 63.9 ms                                                | 62.2 ms: 1.03x faster                                                  |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                                   |
| float                   | 76.3 ms                                                | 71.7 ms: 1.06x faster                                                  |
| generators              | 72.2 ms                                                | 75.7 ms: 1.05x slower                                                  |
| genshi_text             | 22.1 ms                                                | 20.8 ms: 1.06x faster                                                  |
| genshi_xml              | 52.1 ms                                                | 46.6 ms: 1.12x faster                                                  |
| go                      | 143 ms                                                 | 134 ms: 1.07x faster                                                   |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                                  |
| hexiom                  | 6.35 ms                                                | 6.03 ms: 1.05x faster                                                  |
| html5lib                | 63.2 ms                                                | 59.7 ms: 1.06x faster                                                  |
| json                    | 4.95 ms                                                | 4.69 ms: 1.05x faster                                                  |
| json_dumps              | 12.7 ms                                                | 9.35 ms: 1.35x faster                                                  |
| json_loads              | 26.2 us                                                | 24.4 us: 1.07x faster                                                  |
| logging_format          | 6.62 us                                                | 6.22 us: 1.06x faster                                                  |
| logging_silent          | 98.5 ns                                                | 89.4 ns: 1.10x faster                                                  |
| logging_simple          | 6.06 us                                                | 5.66 us: 1.07x faster                                                  |
| mako                    | 9.85 ms                                                | 9.71 ms: 1.01x faster                                                  |
| mdp                     | 2.62 sec                                               | 2.69 sec: 1.02x slower                                                 |
| meteor_contest          | 105 ms                                                 | 103 ms: 1.02x faster                                                   |
| mypy                    | 669 ms                                                 | 809 ms: 1.21x slower                                                   |
| nbody                   | 95.0 ms                                                | 97.0 ms: 1.02x slower                                                  |
| nqueens                 | 85.0 ms                                                | 77.8 ms: 1.09x faster                                                  |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                  |
| pickle                  | 9.79 us                                                | 9.86 us: 1.01x slower                                                  |
| pickle_dict             | 31.4 us                                                | 30.0 us: 1.05x faster                                                  |
| pickle_list             | 4.17 us                                                | 3.99 us: 1.05x faster                                                  |
| pickle_pure_python      | 304 us                                                 | 281 us: 1.08x faster                                                   |
| pidigits                | 199 ms                                                 | 197 ms: 1.01x faster                                                   |
| pprint_safe_repr        | 691 ms                                                 | 663 ms: 1.04x faster                                                   |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.05x faster                                                 |
| pycparser               | 1.17 sec                                               | 1.09 sec: 1.07x faster                                                 |
| pyflate                 | 417 ms                                                 | 401 ms: 1.04x faster                                                   |
| python_startup          | 8.36 ms                                                | 8.54 ms: 1.02x slower                                                  |
| python_startup_no_site  | 5.96 ms                                                | 6.11 ms: 1.02x slower                                                  |
| raytrace                | 290 ms                                                 | 279 ms: 1.04x faster                                                   |
| regex_compile           | 136 ms                                                 | 129 ms: 1.05x faster                                                   |
| regex_effbot            | 3.36 ms                                                | 3.43 ms: 1.02x slower                                                  |
| regex_v8                | 22.3 ms                                                | 21.6 ms: 1.03x faster                                                  |
| richards                | 46.2 ms                                                | 41.2 ms: 1.12x faster                                                  |
| scimark_fft             | 329 ms                                                 | 312 ms: 1.05x faster                                                   |
| scimark_monte_carlo     | 68.3 ms                                                | 64.3 ms: 1.06x faster                                                  |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                   |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.15 ms: 1.06x faster                                                  |
| spectral_norm           | 99.9 ms                                                | 94.5 ms: 1.06x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.02x slower                                                  |
| sqlglot_transpile       | 1.66 ms                                                | 1.68 ms: 1.01x slower                                                  |
| sqlglot_optimize        | 53.0 ms                                                | 50.6 ms: 1.05x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| sqlite_synth            | 2.49 us                                                | 2.61 us: 1.05x slower                                                  |
| sympy_expand            | 472 ms                                                 | 454 ms: 1.04x faster                                                   |
| sympy_integrate         | 20.9 ms                                                | 20.3 ms: 1.03x faster                                                  |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                                   |
| sympy_str               | 287 ms                                                 | 282 ms: 1.02x faster                                                   |
| telco                   | 6.62 ms                                                | 6.22 ms: 1.07x faster                                                  |
| tornado_http            | 96.6 ms                                                | 93.2 ms: 1.04x faster                                                  |
| unpack_sequence         | 43.4 ns                                                | 44.5 ns: 1.03x slower                                                  |
| unpickle_list           | 4.95 us                                                | 4.88 us: 1.02x faster                                                  |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                                   |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                   |
| xml_etree_iterparse     | 103 ms                                                 | 107 ms: 1.04x slower                                                   |
| xml_etree_process       | 53.8 ms                                                | 53.4 ms: 1.01x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (7): async_tree_memoization, bench_mp_pool, regex_dna, scimark_lu, thrift, unpickle, xml_etree_generate
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230113-3.12.0a4+-e5bd5ad/bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
